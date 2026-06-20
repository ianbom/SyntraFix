from datetime import datetime, timezone
from importlib import metadata
from math import ceil
from typing import Any

from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session, selectinload

from app.config import get_settings
from app.models.rag_evaluation import (
    RagArtifactType,
    RagDatasetStatus,
    RagEvaluationArtifact,
    RagEvaluationDataset,
    RagEvaluationDatasetRow,
    RagEvaluationMode,
    RagEvaluationRun,
    RagEvaluationSample,
    RagRunStatus,
)
from app.services.rag_evaluation.aggregation_service import score_distribution

ACTIVE_STATUSES = {
    RagRunStatus.QUEUED,
    RagRunStatus.PREPARING,
    RagRunStatus.RUNNING_RAG,
    RagRunStatus.RUNNING_RAGAS,
    RagRunStatus.AGGREGATING,
}


def create_run(db: Session, dataset_id: int, created_by: int, name: str, description: str | None, evaluation_mode: str | None, evaluator_model: str | None, config: dict[str, Any] | None) -> RagEvaluationRun:
    dataset = db.query(RagEvaluationDataset).filter(RagEvaluationDataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset evaluasi tidak ditemukan")
    if dataset.status != RagDatasetStatus.READY:
        raise HTTPException(status_code=400, detail="Dataset harus berstatus ready sebelum evaluasi")

    mode = RagEvaluationMode(evaluation_mode) if evaluation_mode else dataset.evaluation_mode
    rows_count = db.query(RagEvaluationDatasetRow).filter(
        RagEvaluationDatasetRow.dataset_id == dataset_id,
        RagEvaluationDatasetRow.validation_status == "valid",
    ).count()
    if rows_count == 0:
        raise HTTPException(status_code=400, detail="Dataset tidak memiliki baris valid")

    settings = get_settings()
    snapshot = {
        "generator_model": settings.OLLAMA_GENERATION_MODEL,
        "embedding_model": settings.OLLAMA_EMBEDDING_MODEL,
        "evaluator_model": evaluator_model or settings.OLLAMA_GENERATION_MODEL,
        "ragas_version": _ragas_version(),
        **(config or {}),
    }
    run = RagEvaluationRun(
        dataset_id=dataset_id,
        name=name,
        description=description,
        status=RagRunStatus.QUEUED,
        evaluation_mode=mode,
        total_samples=rows_count,
        processed_samples=0,
        successful_samples=0,
        failed_samples=0,
        progress=0.0,
        generator_model=snapshot["generator_model"],
        embedding_model=snapshot["embedding_model"],
        evaluator_model=snapshot["evaluator_model"],
        ragas_version=snapshot["ragas_version"],
        config_snapshot=snapshot,
        created_by=created_by,
    )
    db.add(run)
    db.commit()
    db.refresh(run)

    from app.tasks.rag_evaluation_tasks import run_rag_evaluation_task

    task = run_rag_evaluation_task.apply_async(args=[run.id], queue="ragas_evaluation")
    run.celery_task_id = task.id
    db.commit()
    db.refresh(run)
    return run


def list_runs(db: Session, page: int, per_page: int, status: str | None = None, dataset_id: int | None = None) -> tuple[list[RagEvaluationRun], int]:
    query = db.query(RagEvaluationRun).options(selectinload(RagEvaluationRun.dataset), selectinload(RagEvaluationRun.artifacts))
    if status:
        query = query.filter(RagEvaluationRun.status == RagRunStatus(status))
    if dataset_id:
        query = query.filter(RagEvaluationRun.dataset_id == dataset_id)
    query = query.order_by(desc(RagEvaluationRun.created_at), desc(RagEvaluationRun.id))
    total = query.count()
    return query.offset((page - 1) * per_page).limit(per_page).all(), total


def get_run_or_404(db: Session, run_id: int) -> RagEvaluationRun:
    run = db.query(RagEvaluationRun).options(
        selectinload(RagEvaluationRun.dataset),
        selectinload(RagEvaluationRun.artifacts),
    ).filter(RagEvaluationRun.id == run_id).first()
    if not run:
        raise HTTPException(status_code=404, detail="Evaluation run tidak ditemukan")
    return run


def get_latest_completed_run(db: Session) -> RagEvaluationRun | None:
    return db.query(RagEvaluationRun).options(selectinload(RagEvaluationRun.dataset), selectinload(RagEvaluationRun.artifacts)).filter(
        RagEvaluationRun.status == RagRunStatus.COMPLETED
    ).order_by(desc(RagEvaluationRun.completed_at), desc(RagEvaluationRun.id)).first()


def get_active_run(db: Session) -> RagEvaluationRun | None:
    return db.query(RagEvaluationRun).options(selectinload(RagEvaluationRun.dataset), selectinload(RagEvaluationRun.artifacts)).filter(
        RagEvaluationRun.status.in_(ACTIVE_STATUSES)
    ).order_by(desc(RagEvaluationRun.created_at), desc(RagEvaluationRun.id)).first()


def list_samples(db: Session, run_id: int, page: int, per_page: int, status: str | None = None) -> tuple[list[RagEvaluationSample], int]:
    get_run_or_404(db, run_id)
    query = db.query(RagEvaluationSample).filter(RagEvaluationSample.run_id == run_id)
    if status:
        query = query.filter(RagEvaluationSample.status == status)
    query = query.order_by(RagEvaluationSample.sample_index.asc())
    total = query.count()
    return query.offset((page - 1) * per_page).limit(per_page).all(), total


def cancel_run(db: Session, run_id: int) -> RagEvaluationRun:
    run = get_run_or_404(db, run_id)
    if run.status not in ACTIVE_STATUSES:
        raise HTTPException(status_code=400, detail="Run tidak sedang aktif")
    run.status = RagRunStatus.CANCELLED
    run.completed_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(run)
    return run


def dashboard_summary(db: Session) -> dict[str, Any]:
    completed = db.query(RagEvaluationRun).options(selectinload(RagEvaluationRun.dataset), selectinload(RagEvaluationRun.artifacts)).filter(
        RagEvaluationRun.status == RagRunStatus.COMPLETED
    ).order_by(desc(RagEvaluationRun.completed_at), desc(RagEvaluationRun.id)).limit(10).all()
    active = get_active_run(db)
    latest = completed[0] if completed else None
    previous = completed[1] if len(completed) > 1 else None
    return {
        "active_run": to_run_dict(active) if active else None,
        "latest_completed_run": to_run_dict(latest) if latest else None,
        "previous_completed_run": to_run_dict(previous) if previous else None,
        "history": [
            {
                "id": run.id,
                "name": run.name,
                "created_at": run.created_at,
                "total_samples": run.total_samples or 0,
                "faithfulness": run.faithfulness_avg,
                "answer_relevancy": run.answer_relevancy_avg,
                "context_precision": run.context_precision_avg,
                "context_recall": run.context_recall_avg,
            }
            for run in reversed(completed)
        ],
    }


def latest_distribution(db: Session, run_id: int | None = None) -> dict[str, Any]:
    run = get_run_or_404(db, run_id) if run_id else get_latest_completed_run(db)
    if not run:
        return {"run_id": None, "buckets": {}}
    samples = db.query(RagEvaluationSample).filter(RagEvaluationSample.run_id == run.id).all()
    return {"run_id": run.id, "buckets": score_distribution(samples)}


def get_result_artifact(db: Session, run_id: int) -> RagEvaluationArtifact:
    get_run_or_404(db, run_id)
    artifact = db.query(RagEvaluationArtifact).filter(
        RagEvaluationArtifact.run_id == run_id,
        RagEvaluationArtifact.artifact_type == RagArtifactType.RESULT_CSV,
    ).order_by(desc(RagEvaluationArtifact.created_at), desc(RagEvaluationArtifact.id)).first()
    if not artifact:
        raise HTTPException(status_code=404, detail="Result CSV belum tersedia")
    return artifact


def to_run_dict(run: RagEvaluationRun) -> dict[str, Any]:
    return {
        "id": run.id,
        "dataset_id": run.dataset_id,
        "dataset_name": run.dataset.name if run.dataset else None,
        "name": run.name,
        "description": run.description,
        "status": _enum_value(run.status),
        "evaluation_mode": _enum_value(run.evaluation_mode),
        "total_samples": run.total_samples or 0,
        "processed_samples": run.processed_samples or 0,
        "successful_samples": run.successful_samples or 0,
        "failed_samples": run.failed_samples or 0,
        "progress": run.progress or 0.0,
        "faithfulness_avg": run.faithfulness_avg,
        "answer_relevancy_avg": run.answer_relevancy_avg,
        "context_precision_avg": run.context_precision_avg,
        "context_recall_avg": run.context_recall_avg,
        "generator_model": run.generator_model,
        "embedding_model": run.embedding_model,
        "evaluator_model": run.evaluator_model,
        "ragas_version": run.ragas_version,
        "config_snapshot": run.config_snapshot,
        "celery_task_id": run.celery_task_id,
        "created_by": run.created_by,
        "started_at": run.started_at,
        "completed_at": run.completed_at,
        "error_message": run.error_message,
        "created_at": run.created_at,
        "artifacts": run.artifacts,
    }


def pages(total: int, per_page: int) -> int:
    return max(1, ceil(total / per_page)) if total else 1


def _ragas_version() -> str | None:
    try:
        return metadata.version("ragas")
    except metadata.PackageNotFoundError:
        return None


def _enum_value(value):
    return getattr(value, "value", value)
