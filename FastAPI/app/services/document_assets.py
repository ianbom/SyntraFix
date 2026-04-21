"""Build table and image chunks from extracted PDF assets."""
import asyncio
import base64
from typing import Any, Dict, List, Optional

from app.models.document_chunk import ChunkType
from app.services.llm import generate_response


def _run_async(coro):
    """Run an async coroutine in a sync context."""
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


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
