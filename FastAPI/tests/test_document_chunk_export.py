from pathlib import Path

from app.services.document_chunk_export import (
    build_chunk_content_markdown,
    build_ragas_markdown,
    export_document_chunk_markdown_files,
    sanitize_markdown_filename,
)


def test_sanitize_markdown_filename_removes_windows_reserved_characters():
    assert sanitize_markdown_filename('A/B:C*D?"E<F>G|') == "A_B_C_D__E_F_G_"


def test_build_chunk_content_markdown_contains_only_chunk_content():
    chunks = [
        {"content": "Konten chunk pertama.", "chunk_index": 0},
        {"content": "Konten chunk kedua.", "chunk_index": 1},
    ]

    markdown = build_chunk_content_markdown(chunks)

    assert markdown == "Konten chunk pertama.\n\n---\n\nKonten chunk kedua.\n"
    assert "chunk_index" not in markdown
    assert "possibly_questions" not in markdown


def test_build_ragas_markdown_contains_questions_and_contexts():
    chunks = [
        {
            "content": "CNN digunakan untuk mendeteksi kanker pada citra medis.",
            "_possibly_questions": [
                "Apa kegunaan CNN dalam dokumen Pengembangan Deteksi Kanker?",
            ],
        }
    ]

    markdown = build_ragas_markdown(chunks)

    assert "## RAGAS Item 1" in markdown
    assert "question:" in markdown
    assert "Apa kegunaan CNN dalam dokumen Pengembangan Deteksi Kanker?" in markdown
    assert "contexts:" in markdown
    assert "CNN digunakan untuk mendeteksi kanker pada citra medis." in markdown


def test_export_document_chunk_markdown_files_writes_two_files(tmp_path):
    chunks = [
        {
            "content": "Konten chunk pertama.",
            "_possibly_questions": ["Apa isi chunk pertama?"],
        }
    ]

    content_path, ragas_path = export_document_chunk_markdown_files(
        document_title="Pengembangan: Deteksi/Kanker",
        chunks=chunks,
        output_dir=tmp_path,
    )

    assert content_path == tmp_path / "Pengembangan_ Deteksi_Kanker.md"
    assert ragas_path == tmp_path / "Pengembangan_ Deteksi_Kanker_ragas.md"
    assert content_path.read_text(encoding="utf-8") == "Konten chunk pertama.\n"
    assert "Apa isi chunk pertama?" in ragas_path.read_text(encoding="utf-8")
