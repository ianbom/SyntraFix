"""Embedding service using Ollama with nomic-embed-text model."""
import requests
import time
import google.generativeai as genai
from typing import Optional
from app.config import get_settings

settings = get_settings()


def _print_embedding_timing(function_name: str, elapsed_seconds: float):
    print(f"[SERVICE TIMING] {function_name}: {elapsed_seconds:.4f}s")


def generate_embedding(text: str, max_retries: int = 3) -> Optional[list[float]]:
    """
    Generate embedding for text using the configured Ollama embedding model.
    Returns a vector matching OLLAMA_EMBEDDING_DIMENSION, or None if failed.
    """
    if not text or not text.strip():
        return None

    started_at = time.perf_counter()
    # Truncate text if too long (nomic-embed-text has context limit)
    text = text.strip()[:8000]  # Keep first 8000 chars
    
    url = f"{settings.OLLAMA_BASE_URL}/api/embeddings"
    payload = {
        "model": settings.OLLAMA_EMBEDDING_MODEL,
        "prompt": text,
        "output_dimensionality": settings.OLLAMA_EMBEDDING_DIMENSION
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, timeout=60)
            
            if response.status_code == 200:
                data = response.json()
                embedding = data.get("embedding")
                if embedding:
                    expected_dimension = settings.OLLAMA_EMBEDDING_DIMENSION
                    actual_dimension = len(embedding)
                    if actual_dimension != expected_dimension:
                        print(
                            f"Embedding dimension mismatch: expected {expected_dimension}, "
                            f"got {actual_dimension} for model {settings.OLLAMA_EMBEDDING_MODEL}"
                        )
                        return None
                    _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
                    return embedding
                print("No embedding in response")
                _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
                return None
            elif response.status_code == 500:
                error_text = response.text[:200]
                if "memory" in error_text.lower():
                    print(f"Ollama memory error (attempt {attempt + 1}/{max_retries}): {error_text}")
                    # Wait before retry
                    time.sleep(2)
                    continue
                else:
                    print(f"Ollama server error: {error_text}")
                    _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
                    return None
            else:
                print(f"Embedding generation failed: {response.status_code}")
                _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
                return None
                
        except requests.exceptions.ConnectionError:
            print("Cannot connect to Ollama. Make sure Ollama is running.")
            _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
            return None
        except requests.exceptions.Timeout:
            print(f"Ollama request timed out (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
            return None
        except Exception as e:
            print(f"Embedding error: {str(e)}")
            _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
            return None

    _print_embedding_timing("generate_embedding", time.perf_counter() - started_at)
    return None


def generate_embeddings_batch(texts: list[str]) -> list[Optional[list[float]]]:
    """
    Generate embeddings for multiple texts.
    Returns list of embeddings (some may be None if failed).
    """
    return [generate_embedding(text) for text in texts]


def generate_embedding_test(text: str) -> Optional[list[float]]:
    """
    Generate embedding for text using Google Generative AI (Gemini).
    Returns 768-dimensional embedding vector or None if failed.
    """
    api_key = settings.GOOGLE_API_KEY or settings.GEMINI_API_KEY
    if not api_key:
        print("GOOGLE_API_KEY or GEMINI_API_KEY not set")
        return None

    if not text or not text.strip():
        return None

    try:
        genai.configure(api_key=api_key)
        
        result = genai.embed_content(
            model=settings.GOOGLE_EMBEDDING_MODEL,
            content=text,
            task_type="retrieval_document",
            title=None,
            output_dimensionality=768
        )
        
        embedding = result.get('embedding')
        if embedding:
            return embedding
        return None
        
    except Exception as e:
        print(f"Google embedding error: {str(e)}")
        return None

