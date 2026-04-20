"""Document upload validation helpers."""
from fastapi import HTTPException, UploadFile

from app.services.documents.common import MAX_PDF_SIZE

class FileValidator:
    """Handles file validation logic."""
    
    @staticmethod
    def validate_pdf(file: UploadFile) -> None:
        """Validate that file is a PDF."""
        if not file.filename or not file.filename.lower().endswith('.pdf'):
            raise HTTPException(status_code=400, detail="File must be a PDF")
    
    @staticmethod
    def validate_size(content: bytes) -> None:
        """Validate file size."""
        if len(content) > MAX_PDF_SIZE:
            raise HTTPException(
                status_code=400,
                detail=f"File too large. Maximum size: {MAX_PDF_SIZE // (1024 * 1024)}MB"
            )
