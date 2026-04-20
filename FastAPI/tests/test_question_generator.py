from app.services.question_generator import (
    _build_question_prompt,
    _replace_ambiguous_document_references,
)


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
