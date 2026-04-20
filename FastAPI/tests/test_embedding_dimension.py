from app.config import get_settings
from app.models.document_chunk import DocumentChunk
from app.services import embedding as embedding_service


def test_document_chunk_vector_dimensions_follow_config():
    settings = get_settings()

    assert DocumentChunk.__table__.c.embedding.type.dim == settings.OLLAMA_EMBEDDING_DIMENSION
    assert (
        DocumentChunk.__table__.c.possibly_question_embedding.type.dim
        == settings.OLLAMA_EMBEDDING_DIMENSION
    )


def test_default_embedding_config_uses_bge_m3_1024():
    settings = get_settings()

    assert settings.OLLAMA_EMBEDDING_MODEL == "bge-m3:567m"
    assert settings.OLLAMA_EMBEDDING_DIMENSION == 1024


def test_generate_embedding_accepts_matching_dimension(monkeypatch):
    settings = get_settings()
    expected_embedding = [0.1] * settings.OLLAMA_EMBEDDING_DIMENSION

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"embedding": expected_embedding}

    def fake_post(*_args, **_kwargs):
        return FakeResponse()

    monkeypatch.setattr(embedding_service.requests, "post", fake_post)

    assert embedding_service.generate_embedding("contoh teks") == expected_embedding


def test_generate_embedding_rejects_mismatched_dimension(monkeypatch):
    settings = get_settings()
    wrong_dimension = settings.OLLAMA_EMBEDDING_DIMENSION - 1

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"embedding": [0.1] * wrong_dimension}

    def fake_post(*_args, **_kwargs):
        return FakeResponse()

    monkeypatch.setattr(embedding_service.requests, "post", fake_post)

    assert embedding_service.generate_embedding("contoh teks") is None
