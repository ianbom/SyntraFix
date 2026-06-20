import math
from dataclasses import dataclass
from typing import Any, Iterable

METRIC_KEYS = ("faithfulness", "answer_relevancy", "context_precision", "context_recall")


@dataclass
class RunAggregate:
    successful_samples: int
    failed_samples: int
    faithfulness_avg: float | None
    answer_relevancy_avg: float | None
    context_precision_avg: float | None
    context_recall_avg: float | None


def calculate_run_aggregate(samples: Iterable[Any]) -> RunAggregate:
    items = list(samples)
    successful = [sample for sample in items if _get(sample, "status") == "completed"]
    failed_count = sum(1 for sample in items if _get(sample, "status") == "failed")
    averages = {key: _average(_get(sample, key) for sample in successful) for key in METRIC_KEYS}
    return RunAggregate(
        successful_samples=len(successful),
        failed_samples=failed_count,
        faithfulness_avg=averages["faithfulness"],
        answer_relevancy_avg=averages["answer_relevancy"],
        context_precision_avg=averages["context_precision"],
        context_recall_avg=averages["context_recall"],
    )


def score_distribution(samples: Iterable[Any]) -> dict[str, dict[str, int]]:
    buckets = {
        "lt_0_50": {key: 0 for key in METRIC_KEYS},
        "0_50_to_0_80": {key: 0 for key in METRIC_KEYS},
        "gt_0_80": {key: 0 for key in METRIC_KEYS},
    }
    for sample in samples:
        if _get(sample, "status") != "completed":
            continue
        for key in METRIC_KEYS:
            value = _safe_float(_get(sample, key))
            if value is None:
                continue
            if value < 0.5:
                buckets["lt_0_50"][key] += 1
            elif value <= 0.8:
                buckets["0_50_to_0_80"][key] += 1
            else:
                buckets["gt_0_80"][key] += 1
    return buckets


def _average(values: Iterable[Any]) -> float | None:
    numbers = [number for number in (_safe_float(value) for value in values) if number is not None]
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def _safe_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(number):
        return None
    return number


def _get(item: Any, key: str) -> Any:
    if isinstance(item, dict):
        value = item.get(key)
    else:
        value = getattr(item, key, None)
    return getattr(value, "value", value)
