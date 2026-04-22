"""RAGAS evaluation helpers for prompt search."""
import math
from typing import Any, Dict, List, Optional

from app.config import get_settings


METRIC_KEYS = [
    "faithfulness",
    "answer_relevancy",
    "context_precision",
    "context_recall",
]

SCORE_WEIGHTS = {
    "faithfulness": 0.40,
    "context_recall": 0.25,
    "answer_relevancy": 0.20,
    "context_precision": 0.15,
}


def _safe_float(value: Any) -> Optional[float]:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(number):
        return None
    return number


def calculate_final_score(metrics: Dict[str, Any]) -> Optional[float]:
    """Calculate weighted score from RAGAS metrics."""
    total = 0.0
    for key, weight in SCORE_WEIGHTS.items():
        value = _safe_float(metrics.get(key))
        if value is None:
            return None
        total += value * weight
    return total


def select_best_iteration(iterations: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Select the iteration with the highest non-null final score."""
    scored = [
        item for item in iterations
        if _safe_float(item.get("final_score")) is not None
    ]
    if not scored:
        return iterations[0] if iterations else None
    return max(scored, key=lambda item: float(item["final_score"]))


def evaluate_iteration_with_ragas(
    question: str,
    contexts: List[str],
    answer: str,
    reference: str,
) -> Dict[str, Optional[float]]:
    """Evaluate one prompt-search sample with RAGAS."""
    try:
        from datasets import Dataset
        from langchain_ollama import ChatOllama, OllamaEmbeddings
        from ragas import evaluate
        from ragas.metrics import AnswerRelevancy, ContextPrecision, ContextRecall, Faithfulness
    except ImportError as error:
        raise RuntimeError(
            "RAGAS dependencies are not installed in the FastAPI environment"
        ) from error

    settings = get_settings()
    dataset = Dataset.from_dict(
        {
            "user_input": [question],
            "retrieved_contexts": [contexts],
            "response": [answer],
            "reference": [reference],
            "question": [question],
            "contexts": [contexts],
            "answer": [answer],
            "ground_truth": [reference],
        }
    )

    score = evaluate(
        dataset,
        metrics=[
            Faithfulness(),
            AnswerRelevancy(),
            ContextPrecision(),
            ContextRecall(),
        ],
        llm=ChatOllama(
            model=settings.OLLAMA_GENERATION_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0.1,
        ),
        embeddings=OllamaEmbeddings(
            model=settings.OLLAMA_EMBEDDING_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
        ),
        batch_size=1,
    )
    df = score.to_pandas()
    row = df.iloc[0].to_dict()
    return {key: _safe_float(row.get(key)) for key in METRIC_KEYS}

