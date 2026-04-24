"""Celery tasks for background document processing."""
import asyncio
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
from app.services.embedding_text import build_embedding_text
from app.services.document_assets import _build_image_chunks, _build_table_chunks
# from app.services.document_chunk_export import export_document_chunk_markdown_files
from app.services.question_generator import _build_fallback_questions, generate_possibly_questions
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
    6. Generate content embeddings
    7. Persist chunks and mark document complete
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

        # Markdown export for chunk inspection is disabled.
        # Uncomment this block when manual PDF coverage/RAGAS debugging is needed.
        # content_export_path, ragas_export_path = export_document_chunk_markdown_files(
        #     metadata.get("title") or document.title or f"document_{document_id}",
        #     chunks,
        # )
        # print(f"  Chunk content markdown exported to: {content_export_path}")
        # print(f"  RAGAS markdown exported to: {ragas_export_path}")

        # Step 6: Generate content embeddings
        print("[6/7] Generating content embeddings...")
        for i, chunk_data in enumerate(chunks):
            try:
                embedding_text = build_embedding_text(chunk_data)
                chunk_data["_embedding"] = generate_embedding(embedding_text)
            except Exception:
                chunk_data["_embedding"] = None
                raise

            if (i + 1) % 5 == 0 or (i + 1) == total_chunks:
                _update_processing_state(
                    db,
                    document_id,
                    progress=_calculate_phase_progress(65, 90, i, total_chunks),
                )

        if total_chunks == 0:
            _update_processing_state(db, document_id, progress=90)

        # Step 7: Persist chunks
        print("[7/7] Saving chunks to database...")
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
                possibly_questions=None,
                possibly_question_embedding=None,
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


def _chunk_has_possibly_questions(chunk: DocumentChunk) -> bool:
    """Return True when both generated questions and their embedding are present."""
    questions = chunk.possibly_questions
    return bool(questions) and chunk.possibly_question_embedding is not None


@shared_task(name="generate_possibly_questions_task", bind=True, max_retries=2)
def generate_possibly_questions_task(self, document_id: int):
    """Generate possibly questions for one document after ingestion has completed."""
    db = SessionLocal()

    try:
        document = db.query(Document).filter(Document.id == document_id).first()
        if not document:
            print(f"Document {document_id} not found for possibly question generation")
            return {"status": "error", "document_id": document_id, "message": "Document not found"}

        eligible_chunks = (
            db.query(DocumentChunk)
            .filter(
                DocumentChunk.document_id == document_id,
                DocumentChunk.content.isnot(None),
                DocumentChunk.content != "",
                DocumentChunk.token_count >= 30,
            )
            .order_by(DocumentChunk.chunk_index.asc())
            .all()
        )
        chunks_to_update = [
            chunk for chunk in eligible_chunks if not _chunk_has_possibly_questions(chunk)
        ]

        print(f"{'='*60}")
        print(
            f"CELERY TASK: Generating possibly questions for document {document_id} "
            f"({len(chunks_to_update)}/{len(eligible_chunks)} missing)"
        )
        print(f"{'='*60}")

        updated_count = 0
        for i, chunk in enumerate(chunks_to_update):
            content = chunk.content or ""
            questions = chunk.possibly_questions if chunk.possibly_questions else None

            try:
                if not questions:
                    questions = _run_async(
                        generate_possibly_questions(
                            chunk_content=content,
                            section_title=chunk.section_title,
                            document_title=(chunk.chunk_metadata or {}).get("source_document")
                            or document.title,
                        )
                    )

                if not questions:
                    questions = _build_fallback_questions(
                        content,
                        section_title=chunk.section_title,
                        document_title=(chunk.chunk_metadata or {}).get("source_document")
                        or document.title,
                    )

                if questions:
                    chunk.possibly_questions = questions
                    if chunk.possibly_question_embedding is None:
                        chunk.possibly_question_embedding = generate_embedding(" ".join(questions))
                    if _chunk_has_possibly_questions(chunk):
                        updated_count += 1
            except Exception as e:
                print(f"  Warning: possibly question generation failed for chunk {chunk.id}: {e}")

            if (i + 1) % 5 == 0 or (i + 1) == len(chunks_to_update):
                db.commit()
                print(f"  Processed possibly questions {i + 1}/{len(chunks_to_update)}")

        if not chunks_to_update:
            db.commit()

        completed_count = sum(
            1 for chunk in eligible_chunks if _chunk_has_possibly_questions(chunk)
        )
        print(f"{'='*60}")
        print(
            f"CELERY TASK COMPLETE: Possibly questions for document {document_id} - "
            f"{completed_count}/{len(eligible_chunks)} complete"
        )
        print(f"{'='*60}")

        return {
            "status": "completed",
            "document_id": document_id,
            "updated_count": updated_count,
            "chunk_count": len(eligible_chunks),
            "possibly_question_count": completed_count,
        }

    except Exception as e:
        db.rollback()
        error_msg = f"{type(e).__name__}: {str(e)}"
        print(f"CELERY TASK FAILED: Possibly questions for document {document_id} - {error_msg}")
        if self.request.retries < self.max_retries:
            raise self.retry(exc=e, countdown=30)
        return {"status": "failed", "document_id": document_id, "error": error_msg}

    finally:
        db.close()

