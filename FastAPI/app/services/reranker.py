"""LLM-based reranking for retrieved document chunks."""
import json
import re
from typing import Any, Dict, List

from app.services.llm import generate_response


def _fallback_rank(candidates: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    ranked = sorted(
        candidates,
        key=lambda item: float(item.get("hybrid_score") or 0.0),
        reverse=True,
    )[:limit]

    return [
        {
            **item,
            "final_score": float(item.get("hybrid_score") or 0.0),
            "rerank_fallback": True,
        }
        for item in ranked
    ]


def _extract_json_array(response_text: str) -> Any:
    text = (response_text or "").strip()
    if not text:
        return None

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    code_match = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", text, re.DOTALL)
    if code_match:
        try:
            return json.loads(code_match.group(1))
        except json.JSONDecodeError:
            pass

    array_match = re.search(r"\[.*\]", text, re.DOTALL)
    if array_match:
        try:
            return json.loads(array_match.group(0))
        except json.JSONDecodeError:
            pass

    return None


def parse_rerank_response(
    response_text: str,
    candidates: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Parse and validate LLM rerank output against the candidate pool."""
    payload = _extract_json_array(response_text)
    if not isinstance(payload, list):
        return []

    candidate_by_id = {
        int(candidate["chunk_id"]): candidate
        for candidate in candidates
        if candidate.get("chunk_id") is not None
    }

    parsed: List[Dict[str, Any]] = []
    seen_ids: set[int] = set()

    for item in payload:
        if not isinstance(item, dict):
            continue

        try:
            chunk_id = int(item.get("chunk_id"))
            score = float(item.get("score"))
        except (TypeError, ValueError):
            continue

        if chunk_id not in candidate_by_id or chunk_id in seen_ids:
            continue

        score = max(0.0, min(score, 1.0))
        seen_ids.add(chunk_id)
        parsed.append(
            {
                **candidate_by_id[chunk_id],
                "rerank_score": score,
                "rerank_reason": str(item.get("reason") or "").strip(),
                "final_score": score,
                "rerank_fallback": False,
            }
        )

    return sorted(parsed, key=lambda item: item["rerank_score"], reverse=True)


def _build_rerank_prompt(query: str, candidates: List[Dict[str, Any]], limit: int) -> str:
    candidate_blocks = []
    for index, candidate in enumerate(candidates, start=1):
        content = " ".join(str(candidate.get("content") or "").split())
        candidate_blocks.append(
            "\n".join(
                [
                    f"Kandidat {index}",
                    f"chunk_id: {candidate.get('chunk_id')}",
                    f"dokumen: {candidate.get('document_title') or 'Unknown Document'}",
                    f"bagian: {candidate.get('section_title') or '-'}",
                    f"halaman: {candidate.get('page_number') or '-'}",
                    f"skor_awal: {float(candidate.get('hybrid_score') or 0.0):.4f}",
                    f"konten: {content[:1200]}",
                ]
            )
        )

    return f"""Anda adalah reranker retrieval untuk chatbot dokumen akademik.

Pertanyaan user:
{query}

Nilai setiap kandidat berdasarkan seberapa langsung kandidat tersebut menjawab pertanyaan user.
Pilih maksimal {limit} kandidat paling relevan.

ATURAN:
- Gunakan hanya chunk_id yang tersedia pada daftar kandidat.
- Score harus angka 0 sampai 1.
- Semakin langsung menjawab pertanyaan, semakin tinggi score.
- Jawab HANYA JSON array, tanpa markdown.

KANDIDAT:
{chr(10).join(candidate_blocks)}

FORMAT:
[
  {{"chunk_id": 1, "score": 0.95, "reason": "Alasan singkat"}},
  {{"chunk_id": 2, "score": 0.70, "reason": "Alasan singkat"}}
]"""


async def rerank_chunks(
    query: str,
    candidates: List[Dict[str, Any]],
    limit: int = 8,
) -> List[Dict[str, Any]]:
    """Rerank retrieved chunks with an LLM, falling back to hybrid order."""
    if not candidates:
        return []

    fallback = _fallback_rank(candidates, limit)
    prompt = _build_rerank_prompt(query, candidates, limit)

    try:
        response_text = await generate_response(prompt)
        parsed = parse_rerank_response(response_text, candidates)
    except Exception as error:
        print(f"  Reranker failed: {error}")
        return fallback

    if not parsed:
        return fallback

    ranked = parsed[:limit]
    ranked_ids = {item["chunk_id"] for item in ranked}

    for item in fallback:
        if len(ranked) >= limit:
            break
        if item["chunk_id"] not in ranked_ids:
            ranked.append(item)
            ranked_ids.add(item["chunk_id"])

    return ranked
