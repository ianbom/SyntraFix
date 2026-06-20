import uuid
from datetime import timedelta
from urllib.parse import urlsplit, urlunsplit

from minio import Minio
from minio.error import S3Error
from fastapi import UploadFile, HTTPException
from app.config import get_settings

settings = get_settings()

# Allowed image types
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


def get_minio_client() -> Minio:
    """Get MinIO client instance."""
    return Minio(
        settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=settings.MINIO_SECURE
    )

def _parse_minio_endpoint(endpoint: str) -> tuple[str, bool]:
    """Return SDK endpoint and secure flag from host[:port] or URL."""
    endpoint = endpoint.strip().rstrip("/")
    if "://" not in endpoint:
        return endpoint, settings.MINIO_SECURE

    parsed = urlsplit(endpoint)
    return parsed.netloc, parsed.scheme == "https"

def get_public_minio_client() -> Minio:
    """Get a MinIO client that signs URLs for the browser-reachable host."""
    endpoint = settings.MINIO_PUBLIC_ENDPOINT or settings.MINIO_ENDPOINT
    public_endpoint, secure = _parse_minio_endpoint(endpoint)
    return Minio(
        public_endpoint,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=secure,
        region="us-east-1",
    )

def get_presigned_object_url(bucket_name: str, object_name: str, expires: timedelta) -> str:
    """Generate a presigned URL whose signature matches the public URL host."""
    return get_public_minio_client().presigned_get_object(
        bucket_name,
        object_name,
        expires=expires,
    )

def rewrite_minio_public_url(url: str) -> str:
    """Rewrite internal MinIO presigned URLs to a browser-reachable endpoint."""
    if not settings.MINIO_PUBLIC_ENDPOINT:
        return url

    source = urlsplit(url)
    public_endpoint = settings.MINIO_PUBLIC_ENDPOINT.strip().rstrip("/")
    if "://" not in public_endpoint:
        public_endpoint = f"{'https' if settings.MINIO_SECURE else 'http'}://{public_endpoint}"
    public = urlsplit(public_endpoint)
    return urlunsplit((public.scheme, public.netloc, source.path, source.query, source.fragment))


def ensure_bucket_exists(client: Minio) -> None:
    """Create bucket if it doesn't exist."""
    try:
        if not client.bucket_exists(settings.MINIO_BUCKET):
            client.make_bucket(settings.MINIO_BUCKET)
    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"MinIO error: {str(e)}")


def validate_image(file: UploadFile) -> None:
    """Validate image file type and size."""
    # Check file extension
    if file.filename:
        extension = file.filename.split(".")[-1].lower()
        if extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
            )
    else:
        raise HTTPException(status_code=400, detail="Filename is required")
    
    # Check content type
    if file.content_type and not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")


async def upload_image(file: UploadFile) -> str:
    """
    Upload image to MinIO.
    Returns the object name (filename in bucket).
    """
    validate_image(file)
    
    # Generate unique filename
    extension = file.filename.split(".")[-1].lower() if file.filename else "jpg"
    unique_filename = f"{uuid.uuid4()}.{extension}"
    
    client = get_minio_client()
    ensure_bucket_exists(client)
    
    try:
        # Read file content
        content = await file.read()
        
        # Check file size
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail=f"File too large. Maximum size: {MAX_FILE_SIZE // (1024 * 1024)}MB"
            )
        
        # Reset file pointer for MinIO
        from io import BytesIO
        file_data = BytesIO(content)
        
        # Upload to MinIO
        client.put_object(
            settings.MINIO_BUCKET,
            unique_filename,
            file_data,
            length=len(content),
            content_type=file.content_type or "image/jpeg"
        )
        
        return unique_filename
        
    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload image: {str(e)}")


def get_image_url(object_name: str) -> str:
    """
    Generate URL for accessing the image.
    Returns a presigned URL or public URL based on configuration.
    """
    try:
        return get_presigned_object_url(
            settings.MINIO_BUCKET,
            object_name,
            expires=timedelta(days=7)
        )
    except S3Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to get image URL: {str(e)}")


def delete_image(object_name: str) -> bool:
    """Delete image from MinIO."""
    client = get_minio_client()
    
    try:
        client.remove_object(settings.MINIO_BUCKET, object_name)
        return True
    except S3Error as e:
        # Log error but don't raise - image might already be deleted
        print(f"Warning: Failed to delete image {object_name}: {str(e)}")
        return False
