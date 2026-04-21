"""Candidate retrieval scoring helpers."""
from typing import Any, Dict, List, Tuple

from app.models.document_chunk import DocumentChunk


def merge_candidate_scores(
    existing: Dict[int, Dict[str, Any]],
    rows: List[Dict[str, Any]],
) -> Dict[int, Dict[str, Any]]:
    """Merge content/question candidate rows by chunk id, keeping best score."""
    merged = dict(existing)

    for row in rows:
        chunk = row["chunk"]
        chunk_id = row.get("chunk_id", getattr(chunk, "id", id(chunk)))
        row = {**row, "chunk_id": chunk_id}

        if chunk_id not in merged or row["hybrid_score"] > merged[chunk_id]["hybrid_score"]:
            merged[chunk_id] = row

    return merged


def select_ranked_candidates(
    candidates: List[Dict[str, Any]],
    limit: int = 8,
    threshold: float = 0.35,
) -> List[Dict[str, Any]]:
    """Apply score threshold and per-document diversification to candidate rows."""
    max_chunks_per_document = 10
    selected: List[Dict[str, Any]] = []
    doc_chunk_count: Dict[int, int] = {}

    for item in sorted(candidates, key=lambda x: x["hybrid_score"], reverse=True):
        if item["hybrid_score"] < threshold:
            break

        doc_id = item["document_id"]
        if doc_chunk_count.get(doc_id, 0) >= max_chunks_per_document:
            continue

        selected.append(item)
        doc_chunk_count[doc_id] = doc_chunk_count.get(doc_id, 0) + 1

        if len(selected) >= limit:
            break

    print(f"  Final retrieved: {len(selected)} chunks (threshold={threshold}, limit={limit})")
    return selected


def candidate_dicts_to_chunks(
    candidates: List[Dict[str, Any]],
) -> Tuple[List[DocumentChunk], List[float]]:
    """Convert scored candidate dictionaries into chunks and scores."""
    chunks = [item["chunk"] for item in candidates]
    similarities = [
        float(item.get("final_score", item.get("hybrid_score", 0.0)) or 0.0)
        for item in candidates
    ]
    return chunks, similarities
