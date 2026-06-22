from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Database
    DATABASE_URL: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 180
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    
    # MinIO
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET: str = "syntra-minio"
    MINIO_DOCUMENTS_BUCKET: str = "documents"
    MINIO_SECURE: bool = False
    
    # GROBID
    GROBID_URL: str = "http://localhost:8070"
    
    # Crossref
    CROSSREF_BASE_URL: str = "https://api.crossref.org"
    CROSSREF_MAILTO: str | None = None
    CROSSREF_TIMEOUT_SECONDS: int = 10
    
    # Celery + RabbitMQ
    CELERY_BROKER_URL: str = "amqp://guest:guest@localhost:5672//"
    
    # Ollama
    # OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_BASE_URL: str = "http://localhost:11435"
    # OLLAMA_EMBEDDING_MODEL: str = "embeddinggemma:latest"
    # OLLAMA_EMBEDDING_DIMENSION: int = 768
    OLLAMA_EMBEDDING_MODEL: str = "bge-m3:567m"
    OLLAMA_GENERATION_MODEL: str = "llama3.1:8b-instruct-q8_0"
    OLLAMA_EMBEDDING_DIMENSION: int = 1024

    # Google Gemini
    GOOGLE_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    GOOGLE_EMBEDDING_MODEL: str = "models/gemini-embedding-001"
    GOOGLE_GENERATION_MODEL: str = "models/gemini-2.5-flash"
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
