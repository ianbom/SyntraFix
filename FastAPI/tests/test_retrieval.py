from app.models.document_chunk import ChunkType
from app.models.document_chunk import DocumentChunk
from app.services import chat as chat_module
from app.services.chat import ChatService
from app.tasks.document_tasks import build_embedding_text


def make_chunk(chunk_id, document_id, chunk_index, content=None, chunk_type=ChunkType.PARAGRAPH):
    chunk = DocumentChunk()
    chunk.id = chunk_id
    chunk.document_id = document_id
    chunk.chunk_index = chunk_index
    chunk.content = content or f"Konten chunk {chunk_index}"
    chunk.chunk_type = chunk_type
    chunk.page_number = chunk_index + 1
    chunk.section_title = "Metode"
    return chunk


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


def test_context_window_expansion_adds_previous_and_next_chunk(monkeypatch):
    parent = make_chunk(10, document_id=1, chunk_index=5)
    previous = make_chunk(9, document_id=1, chunk_index=4)
    next_chunk = make_chunk(11, document_id=1, chunk_index=6)
    service = ChatService(db=None)

    monkeypatch.setattr(
        service,
        "_fetch_context_window_chunks",
        lambda chunk, window_size: [previous, parent, next_chunk],
    )

    expanded = service._expand_context_window([
        {
            "chunk": parent,
            "chunk_id": parent.id,
            "document_id": parent.document_id,
            "hybrid_score": 0.9,
            "final_score": 0.8,
        }
    ])

    assert [item["chunk"].id for item in expanded] == [previous.id, parent.id, next_chunk.id]
    assert expanded[0]["context_window_neighbor"] is True
    assert expanded[0]["context_window_offset"] == -1
    assert expanded[0]["context_window_parent_chunk_id"] == parent.id
    assert expanded[0]["final_score"] == 0.8 * 0.85
    assert "context_window_neighbor" not in expanded[1]
    assert expanded[2]["context_window_offset"] == 1


def test_context_window_expansion_only_uses_top_five_parents(monkeypatch):
    parents = [make_chunk(100 + index, document_id=1, chunk_index=index) for index in range(6)]
    service = ChatService(db=None)
    fetched_parent_ids = []

    def fake_fetch(chunk, _window_size):
        fetched_parent_ids.append(chunk.id)
        return [chunk]

    monkeypatch.setattr(service, "_fetch_context_window_chunks", fake_fetch)

    service._expand_context_window([
        {
            "chunk": chunk,
            "chunk_id": chunk.id,
            "document_id": chunk.document_id,
            "hybrid_score": 1.0 - (index * 0.01),
            "final_score": 1.0 - (index * 0.01),
        }
        for index, chunk in enumerate(parents)
    ])

    assert fetched_parent_ids == [chunk.id for chunk in parents[:5]]


def test_context_window_expansion_deduplicates_existing_reranked_chunks(monkeypatch):
    first = make_chunk(20, document_id=1, chunk_index=5)
    second = make_chunk(21, document_id=1, chunk_index=6)
    service = ChatService(db=None)

    def fake_fetch(chunk, _window_size):
        if chunk.id == first.id:
            return [first, second]
        return [first, second]

    monkeypatch.setattr(service, "_fetch_context_window_chunks", fake_fetch)

    expanded = service._expand_context_window([
        {"chunk": first, "chunk_id": first.id, "document_id": 1, "hybrid_score": 0.9, "final_score": 0.9},
        {"chunk": second, "chunk_id": second.id, "document_id": 1, "hybrid_score": 0.8, "final_score": 0.8},
    ])

    assert [item["chunk"].id for item in expanded] == [first.id, second.id]


def test_context_window_expansion_filters_noisy_visual_neighbors(monkeypatch):
    parent = make_chunk(30, document_id=1, chunk_index=5)
    noisy = make_chunk(
        31,
        document_id=1,
        chunk_index=6,
        content="Maaf, saya tidak dapat menginterpretasikan gambar tersebut.",
        chunk_type=ChunkType.IMAGE,
    )
    service = ChatService(db=None)

    monkeypatch.setattr(service, "_fetch_context_window_chunks", lambda _chunk, _window_size: [parent, noisy])

    expanded = service._expand_context_window([
        {"chunk": parent, "chunk_id": parent.id, "document_id": 1, "hybrid_score": 0.9, "final_score": 0.9}
    ])

    assert [item["chunk"].id for item in expanded] == [parent.id]


async def fake_rerank_chunks(_query, candidates, limit=8):
    return candidates


def test_retrieve_and_rerank_expands_context_window_after_rerank(monkeypatch):
    parent = make_chunk(40, document_id=1, chunk_index=5)
    candidate = {
        "chunk": parent,
        "chunk_id": parent.id,
        "document_id": parent.document_id,
        "hybrid_score": 0.9,
        "final_score": 0.9,
    }
    service = ChatService(db=None)
    expansion_called = {"value": False}

    monkeypatch.setattr(service, "_retrieve_relevant_chunk_candidates", lambda **_kwargs: [candidate])
    monkeypatch.setattr(service, "_select_ranked_candidates", lambda *_args, **_kwargs: [candidate])
    monkeypatch.setattr(chat_module, "rerank_chunks", fake_rerank_chunks)

    def fake_expand(candidates):
        expansion_called["value"] = True
        return candidates

    monkeypatch.setattr(service, "_expand_context_window", fake_expand)

    import asyncio

    chunks, scores = asyncio.run(service._retrieve_and_rerank_chunks("apa itu cnn"))

    assert expansion_called["value"] is True
    assert chunks == [parent]
    assert scores == [0.9]

