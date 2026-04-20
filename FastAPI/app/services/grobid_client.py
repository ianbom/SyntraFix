"""HTTP client helpers for the GROBID service."""
import requests
from fastapi import HTTPException

from app.config import get_settings

settings = get_settings()


def post_grobid(
    endpoint: str,
    file_bytes: bytes,
    timeout: int = 60,
    data: dict | None = None,
    connection_error_detail: str = "GROBID service is not available.",
    timeout_detail: str = "GROBID request timed out.",
):
    """Post a PDF to a GROBID endpoint and return the raw response."""
    url = f"{settings.GROBID_URL}/api/{endpoint}"

    try:
        return requests.post(
            url,
            files={'input': ("document.pdf", file_bytes)},
            data=data,
            headers={'Accept': 'application/xml'},
            timeout=timeout,
        )
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail=connection_error_detail)
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail=timeout_detail)
