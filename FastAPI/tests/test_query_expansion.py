import pytest

from app.services import chat as chat_module
from app.services.chat import ChatService


@pytest.mark.asyncio
async def test_expand_query_returns_indonesian_and_english_variations(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        return (
            "Bahasa Indonesia: Apa manfaat CNN untuk deteksi kanker?\n"
            "English: What are the benefits of CNN for cancer detection?"
        )

    monkeypatch.setattr(chat_module, "generate_response", fake_generate_response)

    expanded = await ChatService(db=None)._expand_query("apa kegunaan cnn dalam deteksi kanker")

    assert expanded == [
        "apa kegunaan cnn dalam deteksi kanker",
        "Apa manfaat CNN untuk deteksi kanker?",
        "What are the benefits of CNN for cancer detection?",
    ]


@pytest.mark.asyncio
async def test_expand_query_fallback_still_includes_indonesian_and_english(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        return "format tidak sesuai"

    monkeypatch.setattr(chat_module, "generate_response", fake_generate_response)

    expanded = await ChatService(db=None)._expand_query("apa kegunaan cnn")

    assert expanded == [
        "apa kegunaan cnn",
        "format tidak sesuai",
        "English query: apa kegunaan cnn",
    ]


@pytest.mark.asyncio
async def test_expand_query_exception_fallback_keeps_bilingual_slots(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        raise RuntimeError("llm down")

    monkeypatch.setattr(chat_module, "generate_response", fake_generate_response)

    expanded = await ChatService(db=None)._expand_query("apa kegunaan cnn")

    assert expanded == [
        "apa kegunaan cnn",
        "apa kegunaan cnn",
        "English query: apa kegunaan cnn",
    ]
