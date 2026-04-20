import pytest

from app.services import reranker


def test_parse_rerank_response_accepts_valid_json_array():
    candidates = [
        {"chunk_id": 10, "hybrid_score": 0.6},
        {"chunk_id": 20, "hybrid_score": 0.5},
    ]
    response_text = """
    [
      {"chunk_id": 20, "score": 0.95, "reason": "Paling sesuai"},
      {"chunk_id": 10, "score": 0.40, "reason": "Kurang spesifik"}
    ]
    """

    parsed = reranker.parse_rerank_response(response_text, candidates)

    assert [item["chunk_id"] for item in parsed] == [20, 10]
    assert parsed[0]["rerank_score"] == 0.95
    assert parsed[0]["rerank_reason"] == "Paling sesuai"


def test_parse_rerank_response_returns_empty_for_invalid_json():
    candidates = [{"chunk_id": 10, "hybrid_score": 0.6}]

    assert reranker.parse_rerank_response("bukan json", candidates) == []


@pytest.mark.asyncio
async def test_rerank_chunks_falls_back_to_hybrid_order_when_llm_fails(monkeypatch):
    async def fake_generate_response(_prompt: str) -> str:
        return "bukan json"

    monkeypatch.setattr(reranker, "generate_response", fake_generate_response)
    candidates = [
        {"chunk_id": 1, "hybrid_score": 0.2, "content": "A"},
        {"chunk_id": 2, "hybrid_score": 0.9, "content": "B"},
    ]

    ranked = await reranker.rerank_chunks("pertanyaan", candidates, limit=2)

    assert [item["chunk_id"] for item in ranked] == [2, 1]
    assert ranked[0]["final_score"] == 0.9
    assert ranked[0]["rerank_fallback"] is True
