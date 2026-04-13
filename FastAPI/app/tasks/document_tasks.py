"""Celery tasks for background document processing."""
import asyncio
import base64
from typing import Optional, Dict, Any, List
from celery import shared_task
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.document import Document
from app.models.document_chunk import DocumentChunk, ChunkType
from app.services.grobid import (
    extract_header, extract_fulltext, extract_references,
    format_for_database, extract_structured_fulltext
)
from app.services.embedding import generate_embedding
from app.services.llm import generate_response
from app.services.question_generator import generate_possibly_questions
from app.services.metadata_extractor import (
    extract_metadata_with_llm, is_metadata_incomplete, merge_metadata
)
from app.services.document import (
    MinIOStorage,
    SmartChunker,
    TextChunker,
    extract_pdf_tables_and_images,
    extract_raw_pdf_text,
    validate_metadata,
)


def _run_async(coro):
    """Run an async coroutine in a sync context (for Celery)."""
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def _clamp_progress(progress: int) -> int:
    """Clamp progress value to 0-100 range."""
    return max(0, min(progress, 100))


def _update_processing_state(
    db: Session,
    document_id: int,
    status: Optional[str] = None,
    progress: Optional[int] = None,
    error: Optional[str] = None,
    clear_error: bool = False,
):
    """Persist processing status/progress/error for a document."""
    doc = db.query(Document).filter(Document.id == document_id).first()
    if doc:
        if status is not None:
            doc.processing_status = status
        if progress is not None:
            doc.processing_progress = _clamp_progress(progress)
        if clear_error:
            doc.processing_error = None
        if error is not None:
            doc.processing_error = error
        db.commit()


def _calculate_phase_progress(
    start_progress: int,
    end_progress: int,
    current_index: int,
    total_items: int,
) -> int:
    """Interpolate progress value for a phase."""
    if total_items <= 0:
        return end_progress

    progress_span = max(0, end_progress - start_progress)
    ratio = (current_index + 1) / total_items
    return min(end_progress, start_progress + int(progress_span * ratio))


def _attach_context_metadata_to_chunks(
    chunks: List[Dict[str, Any]],
    document_title: Optional[str],
) -> None:
    """Store context only in chunk_metadata without injecting headers into content."""
    for chunk_data in chunks:
        raw_content = (chunk_data.get("content") or "").strip()
        if not raw_content:
            continue

        chunk_metadata = chunk_data.get("chunk_metadata") or {}
        section_title = chunk_data.get("section_title") or chunk_metadata.get("section") or "Konten"
        sub_section_title = chunk_metadata.get("sub_section")
        page_number = chunk_data.get("page_number")
        if page_number is None:
            page_number = chunk_metadata.get("page_number")

        chunk_metadata["source_document"] = document_title
        chunk_metadata["section"] = section_title
        if sub_section_title:
            chunk_metadata["sub_section"] = sub_section_title
        if page_number is not None:
            chunk_metadata["page_number"] = page_number
        chunk_metadata["context_in_metadata"] = True
        chunk_data["chunk_metadata"] = chunk_metadata


def _summarize_table(table_data: Dict[str, Any]) -> str:
    """Fallback compact table summary if LLM output is empty."""
    rows = table_data.get("rows") or []
    row_count = table_data.get("row_count") or len(rows)
    column_count = table_data.get("column_count") or (len(rows[0]) if rows else 0)
    caption = table_data.get("caption") or f"Tabel {table_data.get('table_index') or ''}".strip()

    headers = []
    if rows:
        headers = [cell for cell in rows[0] if cell][:6]

    preview_rows = rows[1:4] if len(rows) > 1 else rows[:3]
    preview_values = []
    for row in preview_rows:
        cleaned = [cell for cell in row if cell]
        if cleaned:
            preview_values.append("; ".join(cleaned[:6]))

    parts = [f"{caption} menampilkan {row_count} baris dan {column_count} kolom."]
    if headers:
        parts.append("Kolom utama: " + ", ".join(headers) + ".")
    if preview_values:
        parts.append("Cuplikan data: " + " | ".join(preview_values) + ".")

    return " ".join(parts).strip()


def _table_rows_to_markdown(rows: List[List[str]], max_rows: int = 30, max_cols: int = 10) -> str:
    """Convert table rows into markdown-like text for LLM input."""
    if not rows:
        return "(tabel kosong)"

    limited_rows = rows[:max_rows]
    trimmed_rows: List[List[str]] = []
    for row in limited_rows:
        trimmed_rows.append([str(cell).strip() for cell in row[:max_cols]])

    header = trimmed_rows[0]
    body = trimmed_rows[1:]
    header_line = " | ".join(header)
    sep_line = " | ".join(["---"] * max(1, len(header)))
    body_lines = [" | ".join(row) for row in body]

    return "\n".join([header_line, sep_line] + body_lines)


def _sanitize_llm_text(raw_text: Optional[str]) -> str:
    """Normalize and strip markdown fences from LLM output."""
    if not raw_text:
        return ""

    text = raw_text.strip()
    if text.startswith("```"):
        lines = [line for line in text.splitlines() if not line.strip().startswith("```")]
        text = "\n".join(lines).strip()
    return text


def _is_llm_failure_text(text: str) -> bool:
    """Detect known fallback/error responses returned by generate_response."""
    lowered = text.lower()
    failure_markers = (
        "i apologize, but i encountered",
        "maaf, request timeout",
        "encountered an http error",
        "error processing your request",
    )
    return any(marker in lowered for marker in failure_markers)


def _ensure_caption_in_content(caption: str, content: str) -> str:
    """Ensure caption name is explicitly present at the start of chunk content."""
    clean_caption = (caption or "").strip()
    clean_content = (content or "").strip()
    if not clean_caption:
        return clean_content
    if not clean_content:
        return f"{clean_caption}."
    if clean_content.lower().startswith(clean_caption.lower()):
        return clean_content
    return f"{clean_caption} {clean_content}"


async def _describe_table_with_llm(
    table_data: Dict[str, Any],
    document_title: Optional[str],
) -> str:
    """Use LLM to convert extracted table data into narrative text."""
    rows = table_data.get("rows") or []
    page_number = table_data.get("page_number")
    row_count = table_data.get("row_count") or len(rows)
    column_count = table_data.get("column_count") or (len(rows[0]) if rows else 0)
    caption = table_data.get("caption") or "Tabel tanpa nama"
    table_text = _table_rows_to_markdown(rows)

    prompt = f"""Anda adalah analis dokumen akademik.

Dokumen: {document_title or "Unknown Document"}
Halaman: {page_number}
Nama tabel: {caption}
Jumlah baris: {row_count}
Jumlah kolom: {column_count}

Data tabel:
{table_text}

Tugas:
Ubah data tabel di atas menjadi deskripsi teks naratif ringkas dan informatif dalam bahasa Indonesia.
Jelaskan variabel/kolom utama, nilai atau pola penting, serta insight singkat yang bisa dibaca manusia.

Aturan:
- Jawab HANYA dengan teks naratif (tanpa markdown, tanpa bullet, tanpa JSON).
- Kalimat pertama WAJIB diawali nama tabel persis: "{caption}".
- Jika data minim, jelaskan secara jujur berdasarkan data yang tersedia.
"""

    try:
        llm_text = await generate_response(prompt)
        cleaned = _sanitize_llm_text(llm_text)
        if cleaned and _is_llm_failure_text(cleaned):
            return _summarize_table(table_data)
        return _ensure_caption_in_content(caption, cleaned or _summarize_table(table_data))
    except Exception as e:
        print(f"  Warning: table LLM interpretation failed: {e}")
        return _summarize_table(table_data)


def _build_table_chunks(
    tables_data: List[Dict[str, Any]],
    document_title: Optional[str],
) -> List[Dict[str, Any]]:
    """Convert extracted table data into TABLE chunks with text content from LLM."""
    chunks: List[Dict[str, Any]] = []

    for table_data in tables_data:
        caption = (table_data.get("caption") or "").strip()
        if not caption:
            continue

        page_number = table_data.get("page_number")
        section_title = caption
        interpreted_text = _run_async(_describe_table_with_llm(table_data, document_title))
        if not interpreted_text:
            continue

        interpreted_text = _ensure_caption_in_content(caption, interpreted_text)

        chunks.append({
            "chunk_index": 0,
            "content": interpreted_text,
            "token_count": len(interpreted_text.split()),
            "chunk_type": ChunkType.TABLE,
            "page_number": page_number,
            "section_title": section_title,
            "chunk_metadata": {
                "source_document": document_title,
                "section": section_title,
                "page_number": page_number,
                "chunk_strategy": "pymupdf-table-llm-text",
                "caption": caption,
                "table_index": table_data.get("table_index"),
                "row_count": table_data.get("row_count"),
                "column_count": table_data.get("column_count"),
                "context_in_metadata": True,
                "llm_interpreted": True,
            },
        })

    return chunks


def _fallback_image_description(image_data: Dict[str, Any]) -> str:
    """Fallback image text when LLM output is unavailable."""
    caption = image_data.get("caption") or f"Gambar {image_data.get('image_index') or ''}".strip()
    extension = str(image_data.get("extension") or "unknown").upper()
    width = image_data.get("width")
    height = image_data.get("height")
    size_bytes = image_data.get("size_bytes")

    details = [f"{caption} menampilkan visual dengan format {extension}."]
    if width and height:
        details.append(f"Dimensi gambar {width} x {height} piksel.")
    if size_bytes:
        details.append(f"Ukuran file sekitar {size_bytes} bytes.")
    details.append("Deskripsi visual detail tidak tersedia.")
    return " ".join(details)


async def _describe_image_with_llm(
    image_data: Dict[str, Any],
    document_title: Optional[str],
) -> str:
    """Use LLM to convert extracted image data into narrative text."""
    caption = image_data.get("caption") or "Gambar tanpa nama"
    image_bytes = image_data.get("image_bytes")
    if not image_bytes:
        return _fallback_image_description(image_data)

    base64_payload = base64.b64encode(image_bytes).decode("ascii")
    max_base64_chars = 48000
    truncated = len(base64_payload) > max_base64_chars
    if truncated:
        base64_payload = base64_payload[:max_base64_chars]

    prompt = f"""Anda adalah analis visual dokumen akademik.

Dokumen: {document_title or "Unknown Document"}
Halaman: {image_data.get("page_number")}
Nama gambar: {caption}
Index gambar: {image_data.get("image_index")}
Format: {str(image_data.get("extension") or "unknown").upper()}
Dimensi: {image_data.get("width")} x {image_data.get("height")}
Ukuran bytes: {image_data.get("size_bytes")}
Base64 data terpotong: {"ya" if truncated else "tidak"}

Data base64 gambar:
{base64_payload}

Tugas:
Interpretasikan gambar menjadi deskripsi teks naratif dalam bahasa Indonesia.
Jelaskan jenis visual (misalnya grafik, tabel, diagram, foto), elemen yang tampak, angka/label penting (jika ada), dan makna singkat.

Aturan:
- Jawab HANYA dengan teks naratif (tanpa markdown, tanpa bullet, tanpa JSON).
- Kalimat pertama WAJIB diawali nama gambar persis: "{caption}".
- Jika detail visual tidak bisa diidentifikasi, jelaskan keterbatasannya secara eksplisit namun tetap berikan ringkasan yang paling mungkin dari data yang ada.
"""

    try:
        llm_text = await generate_response(prompt)
        cleaned = _sanitize_llm_text(llm_text)
        if cleaned and _is_llm_failure_text(cleaned):
            return _fallback_image_description(image_data)
        return _ensure_caption_in_content(caption, cleaned or _fallback_image_description(image_data))
    except Exception as e:
        print(f"  Warning: image LLM interpretation failed: {e}")
        return _fallback_image_description(image_data)


def _build_image_chunks(
    images_data: List[Dict[str, Any]],
    document_title: Optional[str],
) -> List[Dict[str, Any]]:
    """Convert extracted image data into IMAGE chunks with text content from LLM."""
    chunks: List[Dict[str, Any]] = []

    for image_data in images_data:
        caption = (image_data.get("caption") or "").strip()
        if not caption:
            continue

        page_number = image_data.get("page_number")
        section_title = caption
        interpreted_text = _run_async(_describe_image_with_llm(image_data, document_title))
        if not interpreted_text:
            continue

        interpreted_text = _ensure_caption_in_content(caption, interpreted_text)

        chunks.append({
            "chunk_index": 0,
            "content": interpreted_text,
            "token_count": len(interpreted_text.split()),
            "chunk_type": ChunkType.IMAGE,
            "page_number": page_number,
            "section_title": section_title,
            "chunk_metadata": {
                "source_document": document_title,
                "section": section_title,
                "page_number": page_number,
                "chunk_strategy": "pymupdf-image-llm-text",
                "caption": caption,
                "image_index": image_data.get("image_index"),
                "extension": image_data.get("extension"),
                "width": image_data.get("width"),
                "height": image_data.get("height"),
                "size_bytes": image_data.get("size_bytes"),
                "xref": image_data.get("xref"),
                "context_in_metadata": True,
                "llm_interpreted": True,
            },
        })

    return chunks


@shared_task(name="process_document_task", bind=True, max_retries=2)
def process_document_task(self, document_id: int, file_path: str):
    """
    Background task pipeline for uploaded PDF documents.

    Pipeline stages:
    1. Download source PDF from MinIO
    2. Extract metadata and structure with GROBID
    3. Extract text, tables, and images with PyMuPDF
    4. Merge/validate metadata and update document record
    5. Build smart chunks (text + table + image + references) with context in metadata
    6. Generate hypothetical questions
    7. Generate embeddings
    8. Persist chunks and mark document complete
    """
    db = SessionLocal()
    storage = MinIOStorage()
    
    try:
        # Update status to processing
        _update_processing_state(
            db,
            document_id,
            status="processing",
            progress=0,
            clear_error=True,
        )
        document = db.query(Document).filter(Document.id == document_id).first()
        if not document:
            print(f"Document {document_id} not found")
            return {"status": "error", "message": "Document not found"}
        
        print(f"{'='*60}")
        print(f"CELERY TASK: Processing document {document_id} ({file_path})")
        print(f"{'='*60}")
        
        # Step 1: Download from MinIO
        print("[1/8] Downloading from MinIO...")
        file_content = storage.download_file(file_path)
        _update_processing_state(db, document_id, progress=10)
        print(f"  Downloaded {len(file_content)} bytes")
        
        # Step 2: Extract metadata and structure via GROBID
        print("[2/8] Extracting metadata and structure with GROBID...")
        header = _run_async(extract_header(file_content))
        references = extract_references(file_content)
        fulltext = extract_fulltext(file_content)
        
        # Structured sections for smart chunking
        structured_sections = []
        try:
            structured_sections = extract_structured_fulltext(file_content)
            print(f"  Extracted {len(structured_sections)} structured sections")
        except Exception as e:
            print(f"  Structured extraction failed: {e}")
        
        metadata = format_for_database(header, references)
        metadata["fulltext"] = fulltext or ""
        metadata["structured_sections"] = structured_sections
        _update_processing_state(db, document_id, progress=30)
        
        # Step 3: PyMuPDF extraction for text/table/image data
        print("[3/8] Extracting text, tables, and images with PyMuPDF...")
        raw_pdf_text, pages_data = extract_raw_pdf_text(file_content)
        tables_data, images_data = extract_pdf_tables_and_images(file_content)
        print(
            f"  Extracted assets: tables={len(tables_data)}, "
            f"images={len(images_data)}"
        )
        _update_processing_state(db, document_id, progress=45)
        
        # Step 4: LLM fallback if metadata incomplete + metadata validation
        if is_metadata_incomplete(metadata):
            print("[4/8] Metadata incomplete, using LLM fallback...")
            llm_input_text = raw_pdf_text if raw_pdf_text else (fulltext or "")
            try:
                llm_metadata = _run_async(extract_metadata_with_llm(llm_input_text, metadata))
                if llm_metadata:
                    metadata = merge_metadata(metadata, llm_metadata)
                    print("  LLM metadata merge complete")
            except Exception as e:
                print(f"  LLM metadata extraction failed: {e}")
        
        # Validate metadata
        metadata = validate_metadata(metadata, raw_pdf_text or fulltext or "")
        
        # Update document with extracted metadata
        print("[4/8] Updating document metadata...")
        document.title = metadata["title"]
        document.creator = metadata.get("creator")
        document.keywords = metadata.get("keywords")
        document.description = metadata.get("description")
        document.publisher = metadata.get("publisher")
        document.contributor = metadata.get("contributor")
        document.date = metadata.get("date")
        document.format = metadata.get("format", "application/pdf")
        document.identifier = metadata.get("identifier")
        document.source = metadata.get("source")
        document.language = metadata.get("language")
        document.relation = metadata.get("relation")
        document.coverage = metadata.get("coverage")
        document.rights = metadata.get("rights")
        document.doi = metadata.get("doi")
        document.abstract = metadata.get("abstract")
        document.citation_count = metadata.get("citation_count", 0)
        document.is_metadata_complete = bool(metadata.get("title") and metadata.get("creator"))
        db.commit()
        _update_processing_state(db, document_id, progress=55)
        
        # Step 5: Smart chunking + table/image chunks (all content as plain text)
        print("[5/8] Building smart chunks...")
        
        
        chunks = []
        if structured_sections:
            print("  Using SMART CHUNKING")
            smart_chunker = SmartChunker()
            chunks = smart_chunker.chunk_structured_sections(
                sections=structured_sections,
                document_title=metadata.get("title"),
                pages_data=pages_data,
            )
        
        if not chunks:
            print("  Falling back to LEGACY CHUNKING")
            chunker = TextChunker()
            chunks = chunker.chunk_text(metadata.get("fulltext", ""), document_title=metadata["title"])
            
            # Add abstract chunk
            if metadata.get("abstract"):
                abstract_chunk = TextChunker.create_abstract_chunk(metadata["abstract"], metadata["title"])
                chunks.insert(0, abstract_chunk)
                TextChunker.reindex_chunks(chunks)
            
            # Add title chunk
            if metadata.get("title"):
                title_chunk = TextChunker.create_title_chunk(
                    metadata["title"], metadata.get("creator"), metadata.get("doi")
                )
                chunks.insert(0, title_chunk)
                TextChunker.reindex_chunks(chunks)
        
        # Attach document/section/page context to metadata only (no header in content)
        _attach_context_metadata_to_chunks(chunks, metadata.get("title"))

        # Add visual chunks interpreted by LLM (table + image -> text)
        table_chunks = _build_table_chunks(tables_data, metadata.get("title"))
        image_chunks = _build_image_chunks(images_data, metadata.get("title"))
        chunks.extend(table_chunks)
        chunks.extend(image_chunks)

        # Re-index all chunks after merge
        for i, chunk_data in enumerate(chunks):
            chunk_data["chunk_index"] = i

        print(
            f"  Created {len(chunks)} chunks "
            f"(text={len(chunks) - len(table_chunks) - len(image_chunks)}, "
            f"table={len(table_chunks)}, image={len(image_chunks)})"
        )
        _update_processing_state(db, document_id, progress=65)
        
        total_chunks = len(chunks)

        # Step 6: Generate hypothetical questions
        print("[6/8] Generating hypothetical questions...")
        for i, chunk_data in enumerate(chunks):
            content = chunk_data.get("content") or ""
            possibly_questions = None
            possibly_question_embedding = None

            try:
                section_title = chunk_data.get("section_title")
                doc_title = chunk_data.get("chunk_metadata", {}).get("source_document")
                questions = _run_async(generate_possibly_questions(
                    chunk_content=content,
                    section_title=section_title,
                    document_title=doc_title,
                ))
                if questions:
                    possibly_questions = questions
                    combined_questions = " ".join(questions)
                    possibly_question_embedding = generate_embedding(combined_questions)
            except Exception as e:
                print(f"  Warning: question generation failed for chunk {i+1}: {e}")

            chunk_data["_possibly_questions"] = possibly_questions
            chunk_data["_possibly_question_embedding"] = possibly_question_embedding

            if (i + 1) % 5 == 0 or (i + 1) == total_chunks:
                _update_processing_state(
                    db,
                    document_id,
                    progress=_calculate_phase_progress(65, 75, i, total_chunks),
                )

        if total_chunks == 0:
            _update_processing_state(db, document_id, progress=75)

        # Step 7: Generate content embeddings
        print("[7/8] Generating content embeddings...")
        for i, chunk_data in enumerate(chunks):
            try:
                chunk_data["_embedding"] = generate_embedding(chunk_data["content"])
            except Exception:
                chunk_data["_embedding"] = None
                raise

            if (i + 1) % 5 == 0 or (i + 1) == total_chunks:
                _update_processing_state(
                    db,
                    document_id,
                    progress=_calculate_phase_progress(75, 90, i, total_chunks),
                )

        if total_chunks == 0:
            _update_processing_state(db, document_id, progress=90)

        # Step 8: Persist chunks
        print("[8/8] Saving chunks to database...")
        total_chunks = len(chunks)

        for i, chunk_data in enumerate(chunks):
            # Create chunk record
            chunk = DocumentChunk(
                document_id=document.id,
                chunk_index=chunk_data["chunk_index"],
                content=chunk_data["content"],
                token_count=chunk_data.get("token_count", len((chunk_data.get("content") or "").split())),
                embedding=chunk_data.get("_embedding"),
                chunk_type=chunk_data.get("chunk_type", ChunkType.PARAGRAPH),
                page_number=chunk_data.get("page_number"),
                section_title=chunk_data.get("section_title"),
                chunk_metadata=chunk_data.get("chunk_metadata"),
                possibly_questions=chunk_data.get("_possibly_questions"),
                possibly_question_embedding=chunk_data.get("_possibly_question_embedding"),
            )
            db.add(chunk)
            
            if (i + 1) % 5 == 0 or (i + 1) == total_chunks:
                print(f"  Processed chunk {i+1}/{total_chunks}")
                db.flush()
                _update_processing_state(
                    db,
                    document_id,
                    progress=_calculate_phase_progress(90, 95, i, total_chunks),
                )

        if total_chunks == 0:
            _update_processing_state(db, document_id, progress=95)
        
        # Mark as completed
        document.processing_status = "completed"
        document.processing_progress = 100
        document.processing_error = None
        db.commit()
        
        print(f"{'='*60}")
        print(f"CELERY TASK COMPLETE: Document {document_id} - {total_chunks} chunks")
        print(f"{'='*60}")
        
        return {
            "status": "completed",
            "document_id": document_id,
            "chunk_count": total_chunks,
            "title": metadata.get("title", "")[:100]
        }
        
    except Exception as e:
        db.rollback()
        error_msg = f"{type(e).__name__}: {str(e)}"
        print(f"CELERY TASK FAILED: Document {document_id} - {error_msg}")
        _update_processing_state(db, document_id, status="failed", error=error_msg)
        
        # Retry on transient errors
        if self.request.retries < self.max_retries:
            raise self.retry(exc=e, countdown=30)
        
        return {"status": "failed", "document_id": document_id, "error": error_msg}
    
    finally:
        db.close()

