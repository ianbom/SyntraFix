"""Build context-rich text for document chunk embeddings."""
from typing import Any, Dict, List


def build_embedding_text(chunk_data: Dict[str, Any]) -> str:
    """Build context-rich text used only for embedding generation."""
    chunk_metadata = chunk_data.get("chunk_metadata") or {}
    if not isinstance(chunk_metadata, dict):
        chunk_metadata = {}

    content = (chunk_data.get("content") or "").strip()
    document_title = chunk_metadata.get("source_document")
    section_title = chunk_data.get("section_title") or chunk_metadata.get("section")
    sub_section_title = chunk_metadata.get("sub_section")
    page_number = chunk_data.get("page_number")
    if page_number is None:
        page_number = chunk_metadata.get("page_number")

    chunk_type = chunk_data.get("chunk_type")
    chunk_type_value = getattr(chunk_type, "value", chunk_type)

    lines: List[str] = []
    if document_title:
        lines.append(f"Judul Dokumen: {document_title}")
    if section_title:
        lines.append(f"Bagian: {section_title}")
    if sub_section_title:
        lines.append(f"Subbagian: {sub_section_title}")
    if chunk_type_value:
        lines.append(f"Tipe Konten: {chunk_type_value}")
    if page_number is not None:
        lines.append(f"Halaman: {page_number}")

    if lines:
        embedding_text = "\n".join(lines) + f"\n\nKonten:\n{content}"
    else:
        embedding_text = f"Konten:\n{content}"

    chunk_metadata["embedding_text"] = embedding_text
    chunk_data["chunk_metadata"] = chunk_metadata

    return embedding_text
