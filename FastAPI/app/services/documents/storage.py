"""MinIO-backed document storage helpers."""
import uuid
from datetime import timedelta
from io import BytesIO

from fastapi import HTTPException

from app.config import get_settings
from app.services.minio import get_minio_client, get_presigned_object_url

settings = get_settings()

class MinIOStorage:
    """Handles MinIO storage operations."""
    
    def __init__(self):
        self.client = get_minio_client()
        self.bucket = settings.MINIO_DOCUMENTS_BUCKET
    
    def ensure_bucket_exists(self) -> None:
        """Create bucket if it doesn't exist."""
        try:
            if not self.client.bucket_exists(self.bucket):
                self.client.make_bucket(self.bucket)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"MinIO error: {str(e)}")
    
    def upload_file(self, content: bytes, original_filename: str) -> str:
        """Upload file to MinIO. Returns unique filename."""
        extension = original_filename.split(".")[-1].lower() if original_filename else "pdf"
        unique_filename = f"{uuid.uuid4()}.{extension}"
        
        self.ensure_bucket_exists()
        
        try:
            self.client.put_object(
                self.bucket,
                unique_filename,
                BytesIO(content),
                length=len(content),
                content_type="application/pdf"
            )
            return unique_filename
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to upload PDF: {str(e)}")

    def upload_binary(
        self,
        content: bytes,
        extension: str,
        prefix: str = "",
        content_type: str = "application/octet-stream",
    ) -> str:
        """Upload arbitrary binary content to MinIO and return object path."""
        normalized_ext = (extension or "bin").strip().lower().lstrip(".")
        object_name = f"{uuid.uuid4()}.{normalized_ext}"

        normalized_prefix = prefix.strip().strip("/").replace("\\", "/") if prefix else ""
        if normalized_prefix:
            object_name = f"{normalized_prefix}/{object_name}"

        self.ensure_bucket_exists()

        try:
            self.client.put_object(
                self.bucket,
                object_name,
                BytesIO(content),
                length=len(content),
                content_type=content_type,
            )
            return object_name
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to upload binary file: {str(e)}")
    
    def delete_file(self, file_path: str) -> bool:
        """Delete file from MinIO."""
        try:
            self.client.remove_object(self.bucket, file_path)
            return True
        except Exception:
            return False
    
    def get_download_url(self, file_path: str, expires_hours: int = 1) -> str:
        """Get presigned download URL."""
        try:
            return get_presigned_object_url(
                self.bucket,
                file_path,
                expires=timedelta(hours=expires_hours)
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to get download URL: {str(e)}")
    
    def download_file(self, file_path: str) -> bytes:
        """Download file content from MinIO. Returns file bytes."""
        try:
            response = self.client.get_object(self.bucket, file_path)
            try:
                return response.read()
            finally:
                response.close()
                response.release_conn()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to download file: {str(e)}")
