from types import SimpleNamespace

from app.services import ragas_export


def test_format_retrieved_context_prefers_document_chunk_content():
    references = [
        SimpleNamespace(
            chunk_id=10,
            quote="Potongan pendek dari chat_references.",
            document_title="Dokumen CNN",
            page_number=3,
        )
    ]

    markdown = ragas_export._format_retrieved_context(
        references,
        chunk_content_by_id={
            10: "Full content dari document_chunks yang jauh lebih lengkap."
        },
    )

    assert "Full content dari document_chunks yang jauh lebih lengkap." in markdown
    assert "Potongan pendek dari chat_references." not in markdown
    assert "(Dokumen CNN, page 3)" in markdown


def test_format_retrieved_context_falls_back_to_quote_when_chunk_missing():
    references = [
        SimpleNamespace(
            chunk_id=99,
            quote="Fallback quote tetap dipakai.",
            document_title="Dokumen Lama",
            page_number=None,
        )
    ]

    markdown = ragas_export._format_retrieved_context(
        references,
        chunk_content_by_id={},
    )

    assert "Fallback quote tetap dipakai." in markdown
    assert "(Dokumen Lama)" in markdown
