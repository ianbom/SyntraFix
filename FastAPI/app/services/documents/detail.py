"""Document detail serialization helpers."""
from typing import Any, Dict

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.document_chunk import DocumentChunk

def _to_serializable(value: Any) -> Any:
    """Recursively convert values into JSON/Pydantic-serializable types."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, dict):
        return {str(key): _to_serializable(item) for key, item in value.items()}

    if isinstance(value, (list, tuple, set)):
        return [_to_serializable(item) for item in value]

    # Handle numpy-like scalars (e.g. numpy.float32) without importing numpy.
    item_method = getattr(value, "item", None)
    if callable(item_method):
        try:
            return _to_serializable(item_method())
        except Exception:
            pass

    # Handle numpy-like arrays/vectors.
    tolist_method = getattr(value, "tolist", None)
    if callable(tolist_method):
        try:
            return _to_serializable(tolist_method())
        except Exception:
            pass

    try:
        return [_to_serializable(item) for item in list(value)]
    except Exception:
        return str(value)


def _serialize_vector(value: Any) -> Any:
    """Convert vector-like values into JSON-friendly output."""
    return _to_serializable(value)


def get_document_detail_data(db: Session, document_id: int) -> Dict[str, Any]:
    """
    Get complete detail data for one document:
    - all columns from documents table
    - all rows/columns from document_chunks table
    """
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    chunks = (
        db.query(DocumentChunk)
        .filter(DocumentChunk.document_id == document_id)
        .order_by(DocumentChunk.chunk_index.asc(), DocumentChunk.id.asc())
        .all()
    )

    document_payload = {
        "id": document.id,
        "title": document.title,
        "creator": document.creator,
        "keywords": document.keywords,
        "description": document.description,
        "publisher": document.publisher,
        "contributor": document.contributor,
        "date": document.date,
        "type": document.type.value if document.type else None,
        "format": document.format,
        "identifier": document.identifier,
        "source": document.source,
        "language": document.language,
        "relation": document.relation,
        "coverage": document.coverage,
        "rights": document.rights,
        "doi": document.doi,
        "abstract": document.abstract,
        "citation_count": document.citation_count,
        "file_path": document.file_path,
        "is_private": document.is_private,
        "is_metadata_complete": document.is_metadata_complete,
        "processing_status": document.processing_status,
        "processing_progress": document.processing_progress,
        "processing_error": document.processing_error,
        "created_at": document.created_at,
        "updated_at": document.updated_at,
    }

    chunk_payloads = []
    for chunk in chunks:
        chunk_payloads.append({
            "id": chunk.id,
            "document_id": chunk.document_id,
            "chunk_index": chunk.chunk_index,
            "content": chunk.content,
            "token_count": chunk.token_count,
            "embedding": _serialize_vector(chunk.embedding),
            "possibly_questions": _to_serializable(chunk.possibly_questions),
            "possibly_question_embedding": _serialize_vector(chunk.possibly_question_embedding),
            "chunk_metadata": _to_serializable(chunk.chunk_metadata),
            "page_number": chunk.page_number,
            "section_title": chunk.section_title,
            "chunk_type": chunk.chunk_type.value if chunk.chunk_type else None,
            "created_at": chunk.created_at,
            "updated_at": chunk.updated_at,
        })

    return {
        "document": document_payload,
        "chunks": chunk_payloads,
        "chunk_count": len(chunk_payloads),
    }
