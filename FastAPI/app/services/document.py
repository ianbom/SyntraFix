"""Backward-compatible public document service API."""
from typing import Callable, Optional

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document, DocumentType
from app.services.documents.chunking import SmartChunker, TextChunker
from app.services.documents.common import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    ChunkData,
)
from app.services.documents.detail import (
    _serialize_vector,
    _to_serializable,
    get_document_detail_data,
)
from app.services.documents.extraction import (
    build_context_injected_content,
    extract_pdf_tables_and_images,
    extract_raw_pdf_text,
    validate_metadata,
)
from app.services.documents.processing import (
    ChunkProcessor,
    DocumentBuilder,
    DocumentService,
    process_document,
)
from app.services.documents.storage import MinIOStorage
from app.services.documents.validation import FileValidator


def get_document_download_url(file_path: str) -> str:
    """Get presigned URL for downloading a document."""
    storage = MinIOStorage()
    return storage.get_download_url(file_path)


def delete_document_file(file_path: str) -> bool:
    """Delete document file from MinIO."""
    storage = MinIOStorage()
    return storage.delete_file(file_path)


def ensure_documents_bucket_exists(client) -> None:
    """Legacy: Create documents bucket if it doesn't exist."""
    storage = MinIOStorage()
    storage.ensure_bucket_exists()


async def upload_pdf_to_minio(file_content: bytes, original_filename: str) -> str:
    """Legacy: Upload PDF to MinIO."""
    storage = MinIOStorage()
    return storage.upload_file(file_content, original_filename)


def chunk_text(
    text: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP,
    document_title: str = None,
) -> list[dict]:
    """Legacy: Split text into chunks."""
    chunker = TextChunker(chunk_size, overlap)
    return chunker.chunk_text(text, document_title)


__all__ = [
    "ChunkData",
    "ChunkProcessor",
    "DocumentBuilder",
    "DocumentService",
    "FileValidator",
    "MinIOStorage",
    "SmartChunker",
    "TextChunker",
    "build_context_injected_content",
    "chunk_text",
    "delete_document_file",
    "ensure_documents_bucket_exists",
    "extract_pdf_tables_and_images",
    "extract_raw_pdf_text",
    "get_document_detail_data",
    "get_document_download_url",
    "process_document",
    "upload_pdf_to_minio",
    "validate_metadata",
]
