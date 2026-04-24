from app.models.document_chunk import ChunkType
from app.services.chat import ChatService
from app.tasks.document_tasks import build_embedding_text


def test_build_embedding_text_includes_context_and_content():
    chunk_data = {
        "content": "CNN digunakan untuk mengklasifikasikan citra kanker.",
        "chunk_type": ChunkType.PARAGRAPH,
        "page_number": 7,
        "section_title": "Metode",
        "chunk_metadata": {
            "source_document": "Pengembangan Deteksi Kanker",
            "section": "Metode",
            "sub_section": "Convolutional Neural Network",
        },
    }

    embedding_text = build_embedding_text(chunk_data)

    assert "Judul Dokumen: Pengembangan Deteksi Kanker" in embedding_text
    assert "Bagian: Metode" in embedding_text
    assert "Subbagian: Convolutional Neural Network" in embedding_text
    assert "Tipe Konten: paragraph" in embedding_text
    assert "Halaman: 7" in embedding_text
    assert "Konten:\nCNN digunakan untuk mengklasifikasikan citra kanker." in embedding_text
    assert chunk_data["chunk_metadata"]["embedding_text"] == embedding_text


def test_build_embedding_text_handles_missing_metadata():
    chunk_data = {
        "content": "Konten tanpa metadata tetap bisa dibuat embedding.",
        "chunk_metadata": None,
    }

    embedding_text = build_embedding_text(chunk_data)

    assert "Konten:\nKonten tanpa metadata tetap bisa dibuat embedding." in embedding_text
    assert chunk_data["chunk_metadata"]["embedding_text"] == embedding_text


def test_merge_candidate_scores_keeps_question_candidate_when_content_score_is_low():
    service = ChatService(db=None)
    content_chunk = object()
    question_chunk = object()

    merged = service._merge_candidate_scores(
        existing={},
        rows=[
            {
                "chunk": content_chunk,
                "document_id": 1,
                "document_title": "Dokumen A",
                "semantic_score": 0.52,
                "question_score": 0.0,
                "keyword_score": 0.0,
                "hybrid_score": 0.338,
                "retrieval_source": "content",
            },
            {
                "chunk": question_chunk,
                "document_id": 2,
                "document_title": "Pengembangan Deteksi Kanker",
                "semantic_score": 0.20,
                "question_score": 0.88,
                "keyword_score": 0.0,
                "hybrid_score": 0.572,
                "retrieval_source": "question",
            },
        ],
    )

    scored = sorted(merged.values(), key=lambda item: item["hybrid_score"], reverse=True)

    assert scored[0]["chunk"] is question_chunk
    assert scored[0]["retrieval_source"] == "question"
    assert scored[0]["question_score"] == 0.88


def test_noisy_visual_or_table_summary_is_filtered():
    candidate = {
        "chunk_type": ChunkType.IMAGE.value,
        "content": "Maaf, saya tidak dapat menginterpretasikan gambar tersebut.",
    }

    assert ChatService._is_noisy_visual_or_table_summary(candidate) is True


def test_valid_table_chunk_is_not_filtered():
    candidate = {
        "chunk_type": ChunkType.TABLE.value,
        "content": "Tabel hasil eksperimen menunjukkan accuracy CNN sebesar 95%.",
    }

    assert ChatService._is_noisy_visual_or_table_summary(candidate) is False


def test_paragraph_chunk_is_not_filtered_even_with_visual_phrase():
    candidate = {
        "chunk_type": ChunkType.PARAGRAPH.value,
        "content": "Penulis menjelaskan bahwa model tidak dapat melihat fitur tertentu.",
    }

    assert ChatService._is_noisy_visual_or_table_summary(candidate) is False

