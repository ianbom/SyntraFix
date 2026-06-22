import math
import sys
import inspect
from pathlib import Path
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_pipeline_csv_validator_requires_user_input_and_reference():
    from app.services.rag_evaluation.csv_validator import validate_csv_rows

    result = validate_csv_rows(
        rows=[
            {"user_input": "Apa itu RAG?", "reference": "RAG menggabungkan retrieval dan generation."},
            {"user_input": "", "reference": "Jawaban acuan."},
            {"user_input": "Apa itu metadata?", "reference": ""},
        ],
        evaluation_mode="pipeline",
    )

    assert result.total_rows == 3
    assert result.valid_rows == 1
    assert result.invalid_rows == 2
    assert result.rows[0].validation_status == "valid"
    assert result.rows[1].validation_status == "invalid"
    assert "user_input wajib" in result.rows[1].validation_message
    assert "reference wajib" in result.rows[2].validation_message


def test_score_only_csv_validator_requires_json_array_contexts():
    from app.services.rag_evaluation.csv_validator import validate_csv_rows

    result = validate_csv_rows(
        rows=[
            {
                "user_input": "Apa itu RAG?",
                "response": "Jawaban bot.",
                "retrieved_contexts": '["context satu", "context dua"]',
                "reference": "Jawaban acuan.",
            },
            {
                "user_input": "Apa itu DOI?",
                "response": "Jawaban bot.",
                "retrieved_contexts": "bukan json",
                "reference": "Jawaban acuan.",
            },
        ],
        evaluation_mode="score_only",
    )

    assert result.valid_rows == 1
    assert result.invalid_rows == 1
    assert result.rows[0].retrieved_contexts == ["context satu", "context dua"]
    assert "retrieved_contexts harus JSON array" in result.rows[1].validation_message


def test_aggregation_ignores_failed_null_and_nan_scores():
    from app.services.rag_evaluation.aggregation_service import calculate_run_aggregate

    samples = [
        {
            "status": "completed",
            "faithfulness": 0.8,
            "answer_relevancy": 0.7,
            "context_precision": 0.6,
            "context_recall": 0.5,
        },
        {
            "status": "completed",
            "faithfulness": math.nan,
            "answer_relevancy": None,
            "context_precision": 1.0,
            "context_recall": 0.9,
        },
        {
            "status": "failed",
            "faithfulness": 1.0,
            "answer_relevancy": 1.0,
            "context_precision": 1.0,
            "context_recall": 1.0,
        },
    ]

    aggregate = calculate_run_aggregate(samples)

    assert aggregate.successful_samples == 2
    assert aggregate.failed_samples == 1
    assert aggregate.faithfulness_avg == pytest.approx(0.8)
    assert aggregate.answer_relevancy_avg == pytest.approx(0.7)
    assert aggregate.context_precision_avg == pytest.approx(0.8)
    assert aggregate.context_recall_avg == pytest.approx(0.7)


def test_rag_evaluation_route_is_registered_and_admin_protected():
    from app.api.deps import require_admin_user
    from app.main import app

    paths = {route.path for route in app.routes}
    assert "/rag-evaluation/dashboard/summary" in paths
    assert "/rag-evaluation/datasets/upload" in paths
    assert "/rag-evaluation/runs" in paths
    assert "/rag-evaluation/datasets/{dataset_id}/rows/{row_id}" in paths
    row_route_methods = {
        method
        for route in app.routes
        if route.path == "/rag-evaluation/datasets/{dataset_id}/rows/{row_id}"
        for method in route.methods
    }
    assert "DELETE" in row_route_methods

    route = next(route for route in app.routes if route.path == "/rag-evaluation/dashboard/summary")
    dependency_calls = {dependency.call for dependency in route.dependant.dependencies}
    assert require_admin_user in dependency_calls

def test_run_samples_route_supports_all_query_parameter():
    from app.api.routes.rag_evaluations import get_run_samples

    signature = inspect.signature(get_run_samples)

    assert "all_rows" in signature.parameters

def test_dataset_row_delete_service_exists():
    from app.services.rag_evaluation import dataset_service

    assert hasattr(dataset_service, "delete_dataset_row")

def test_dataset_template_defaults_to_score_only_format():
    from app.api.routes.rag_evaluations import download_template

    response = download_template()

    assert response.body.decode("utf-8") == "user_input,response,retrieved_contexts,reference\n"
    assert "rag-evaluation-score-only-template.csv" in response.headers["content-disposition"]

def test_dataset_upload_defaults_to_score_only_mode():
    from app.api.routes.rag_evaluations import upload_dataset

    default = inspect.signature(upload_dataset).parameters["evaluation_mode"].default

    assert default == "score_only"

def test_chat_export_headers_match_score_only_template():
    from app.services.rag_evaluation.chat_exporter import CHAT_EXPORT_HEADERS

    assert CHAT_EXPORT_HEADERS == ["user_input", "response", "retrieved_contexts", "reference"]

def test_chat_export_route_passes_date_range_to_exporter(monkeypatch):
    from app.api.routes import rag_evaluations
    from app.schemas.rag_evaluation import ChatExportRequest

    captured = {}

    def fake_export_chat_csv(db, **kwargs):
        captured["db"] = db
        captured.update(kwargs)
        return b"conversation_id\n"

    monkeypatch.setattr(rag_evaluations, "export_chat_csv", fake_export_chat_csv)

    request = ChatExportRequest(
        date_from=datetime(2026, 6, 1, tzinfo=timezone.utc),
        date_to=datetime(2026, 6, 20, tzinfo=timezone.utc),
        user_ids=[],
        conversation_ids=[],
        only_with_references=False,
        create_dataset=False,
    )

    rag_evaluations.chat_export(request, current_user=SimpleNamespace(id=1), db=SimpleNamespace())

    assert captured["date_from"] == datetime(2026, 6, 1, tzinfo=timezone.utc)
    assert captured["date_to"] == datetime(2026, 6, 20, tzinfo=timezone.utc)

def test_chat_export_date_range_matches_inclusive_bot_created_at():
    from app.services.rag_evaluation.chat_exporter import _is_within_date_range

    assert _is_within_date_range(
        datetime(2026, 6, 10, 12, 0, tzinfo=timezone.utc),
        date_from=datetime(2026, 6, 1, tzinfo=timezone.utc),
        date_to=datetime(2026, 6, 20, 23, 59, 59, tzinfo=timezone.utc),
    ) is True
    assert _is_within_date_range(
        datetime(2026, 5, 31, 23, 59, tzinfo=timezone.utc),
        date_from=datetime(2026, 6, 1, tzinfo=timezone.utc),
        date_to=datetime(2026, 6, 20, 23, 59, 59, tzinfo=timezone.utc),
    ) is False
    assert _is_within_date_range(
        datetime(2026, 6, 21, 0, 0, tzinfo=timezone.utc),
        date_from=datetime(2026, 6, 1, tzinfo=timezone.utc),
        date_to=datetime(2026, 6, 20, 23, 59, 59, tzinfo=timezone.utc),
    ) is False
