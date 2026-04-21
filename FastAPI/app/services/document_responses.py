"""Document response formatting helpers used by API routes."""
from typing import Optional

from app.models.document import Document
from app.schemas.document import DocumentResponse, DocumentTypeEnum

PROCESS_MONITOR_STATUSES = ("processing", "completed", "failed")


def normalize_processing_status(status: Optional[str]) -> str:
    """Normalize processing status to known values."""
    if status in PROCESS_MONITOR_STATUSES:
        return status
    return "processing"


def normalize_processing_progress(progress: Optional[int], status: Optional[str]) -> int:
    """Normalize persisted progress value to 0-100."""
    normalized_status = normalize_processing_status(status)

    if progress is None:
        return 100 if normalized_status == "completed" else 0

    normalized_progress = max(0, min(int(progress), 100))
    if normalized_status == "completed" and normalized_progress < 100:
        return 100

    return normalized_progress


def build_document_response(document: Document, chunk_count: int) -> DocumentResponse:
    """Build DocumentResponse from a Document model."""
    normalized_status = normalize_processing_status(document.processing_status)

    return DocumentResponse(
        id=document.id,
        title=document.title,
        creator=document.creator,
        keywords=document.keywords,
        description=document.description,
        publisher=document.publisher,
        contributor=document.contributor,
        publication_date=document.date,
        type=DocumentTypeEnum(document.type.value) if document.type else DocumentTypeEnum.JOURNAL,
        format=document.format,
        identifier=document.identifier,
        source=document.source,
        language=document.language,
        relation=document.relation,
        coverage=document.coverage,
        rights=document.rights,
        doi=document.doi,
        abstract=document.abstract,
        citation_count=document.citation_count or 0,
        file_path=document.file_path,
        is_private=document.is_private or False,
        is_metadata_complete=document.is_metadata_complete or False,
        processing_status=normalized_status,
        processing_progress=normalize_processing_progress(
            document.processing_progress,
            normalized_status,
        ),
        processing_error=document.processing_error,
        created_at=document.created_at,
        updated_at=document.updated_at,
        chunk_count=chunk_count,
    )
