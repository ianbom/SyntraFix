from app.services.question_generator import (
    _build_fallback_questions,
    _build_question_prompt,
    _replace_ambiguous_document_references,
    generate_possibly_questions,
)
import pytest


def test_replaces_ambiguous_document_references_with_document_title():
    questions = [
        "Apa kegunaan CNN dalam penelitian ini?",
        "Bagaimana metode pada dokumen ini bekerja?",
        "Apa hasil utama studi ini?",
    ]

    result = _replace_ambiguous_document_references(
        questions,
        "Pengembangan Deteksi Kanker",
    )

    assert result == [
        "Apa kegunaan CNN dalam penelitian Pengembangan Deteksi Kanker?",
        "Bagaimana metode pada dokumen Pengembangan Deteksi Kanker bekerja?",
        "Apa hasil utama studi Pengembangan Deteksi Kanker?",
    ]


def test_question_prompt_requires_document_title_when_available():
    prompt = _build_question_prompt(
        "CNN digunakan untuk mendeteksi kanker pada citra medis.",
        document_title="Pengembangan Deteksi Kanker",
        num_questions=1,
    )

    assert "WAJIB menyebut judul dokumen" in prompt
    assert "Pengembangan Deteksi Kanker" in prompt


def test_build_fallback_questions_uses_document_title_and_section():
    content = " ".join(
        [
            "CNN", "digunakan", "untuk", "mendeteksi", "kanker", "pada",
            "citra", "medis", "dengan", "fitur", "visual", "penting",
            "serta", "membantu", "klasifikasi", "berdasarkan", "pola",
            "tekstur", "warna", "bentuk", "jaringan", "sel", "tumor",
            "ganas", "jinak", "melalui", "proses", "pelatihan", "model",
            "mendalam",
        ]
    )
    questions = _build_fallback_questions(
        chunk_content=content,
        section_title="Metode CNN",
        document_title="Pengembangan Deteksi Kanker",
        num_questions=3,
    )

    assert len(questions) == 3
    assert all("Pengembangan Deteksi Kanker" in question for question in questions)
    assert questions[0] == "Apa informasi utama pada bagian Metode CNN dalam dokumen Pengembangan Deteksi Kanker?"


@pytest.mark.asyncio
async def test_generate_possibly_questions_returns_fallback_for_30_words_when_llm_empty(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        return ""

    monkeypatch.setattr("app.services.question_generator.generate_response", fake_generate_response)
    content = " ".join(f"kata{i}" for i in range(30))

    questions = await generate_possibly_questions(
        chunk_content=content,
        section_title="Hasil",
        document_title="Dokumen Uji",
        num_questions=2,
    )

    assert len(questions) == 2
    assert all("Dokumen Uji" in question for question in questions)


@pytest.mark.asyncio
async def test_generate_possibly_questions_returns_empty_below_30_words(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        raise AssertionError("LLM should not be called for short chunks")

    monkeypatch.setattr("app.services.question_generator.generate_response", fake_generate_response)
    content = " ".join(f"kata{i}" for i in range(29))

    assert await generate_possibly_questions(content, document_title="Dokumen Uji") == []
