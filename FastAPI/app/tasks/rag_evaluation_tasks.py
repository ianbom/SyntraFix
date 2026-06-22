import asyncio
import time
from datetime import datetime, timezone

from celery import shared_task
from celery.utils.log import get_task_logger

from app.database import SessionLocal
from app.models.rag_evaluation import (
    RagEvaluationDatasetRow,
    RagEvaluationRun,
    RagEvaluationSample,
    RagRunStatus,
    RagSampleStatus,
)
from app.services.chat import ChatService
from app.services.prompt_search.ragas_evaluator import evaluate_iteration_with_ragas
from app.services.rag_evaluation.aggregation_service import calculate_run_aggregate
from app.services.rag_evaluation.artifact_service import persist_result_artifact

logger = get_task_logger(__name__)


def _run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if loop.is_running():
        new_loop = asyncio.new_event_loop()
        try:
            return new_loop.run_until_complete(coro)
        finally:
            new_loop.close()
    return loop.run_until_complete(coro)


@shared_task(name="run_rag_evaluation_task", bind=True, max_retries=0, time_limit=7200, soft_time_limit=7000)
def run_rag_evaluation_task(self, run_id: int):
    db = SessionLocal()
    try:
        run = db.query(RagEvaluationRun).filter(RagEvaluationRun.id == run_id).first()
        if not run:
            return {"status": "missing", "run_id": run_id}

        run.status = RagRunStatus.PREPARING
        run.started_at = datetime.now(timezone.utc)
        db.commit()

        samples = _ensure_samples(db, run)
        if not samples:
            run.status = RagRunStatus.FAILED
            run.error_message = "Tidak ada sample valid untuk evaluasi"
            run.completed_at = datetime.now(timezone.utc)
            db.commit()
            return {"status": "failed", "run_id": run_id}

        chat_service = ChatService(db)
        for sample in samples:
            db.refresh(run)
            if run.status == RagRunStatus.CANCELLED:
                return {"status": "cancelled", "run_id": run_id}
            if sample.status == RagSampleStatus.COMPLETED:
                continue

            sample.status = RagSampleStatus.PROCESSING
            db.commit()
            try:
                _process_sample(db, run, sample, chat_service)
            except Exception as error:
                logger.exception(
                    "RAG evaluation sample failed run_id=%s sample_index=%s",
                    run.id,
                    sample.sample_index,
                )
                sample.status = RagSampleStatus.FAILED
                sample.error_message = str(error)
                sample.completed_at = datetime.now(timezone.utc)
                db.commit()
            _update_progress(db, run.id)

        _finish_run(db, run.id)
        db.refresh(run)
        return {"status": run.status.value, "run_id": run_id}
    except Exception as error:
        run = db.query(RagEvaluationRun).filter(RagEvaluationRun.id == run_id).first()
        if run:
            run.status = RagRunStatus.FAILED
            run.error_message = str(error)
            run.completed_at = datetime.now(timezone.utc)
            db.commit()
        raise
    finally:
        db.close()


def _ensure_samples(db, run: RagEvaluationRun) -> list[RagEvaluationSample]:
    existing = db.query(RagEvaluationSample).filter(RagEvaluationSample.run_id == run.id).order_by(RagEvaluationSample.sample_index.asc()).all()
    if existing:
        return existing

    rows = db.query(RagEvaluationDatasetRow).filter(
        RagEvaluationDatasetRow.dataset_id == run.dataset_id,
        RagEvaluationDatasetRow.validation_status == "valid",
    ).order_by(RagEvaluationDatasetRow.row_number.asc()).all()
    for index, row in enumerate(rows, start=1):
        db.add(
            RagEvaluationSample(
                run_id=run.id,
                dataset_row_id=row.id,
                sample_index=index,
                user_input=row.user_input,
                reference=row.reference,
                response=row.response,
                retrieved_contexts=row.retrieved_contexts,
                status=RagSampleStatus.PENDING,
            )
        )
    run.total_samples = len(rows)
    db.commit()
    return db.query(RagEvaluationSample).filter(RagEvaluationSample.run_id == run.id).order_by(RagEvaluationSample.sample_index.asc()).all()


def _process_sample(db, run: RagEvaluationRun, sample: RagEvaluationSample, chat_service: ChatService) -> None:
    if run.evaluation_mode.value == "pipeline":
        run.status = RagRunStatus.RUNNING_RAG
        db.commit()
        pipeline_result = _run_async(chat_service.run_rag_pipeline(sample.user_input))
        sample.response = pipeline_result.response
        sample.retrieved_contexts = pipeline_result.retrieved_contexts
        sample.references_metadata = pipeline_result.references_metadata
        sample.rag_duration_seconds = pipeline_result.rag_duration_seconds
    elif not sample.response or not sample.retrieved_contexts:
        raise ValueError("Score-only sample harus memiliki response dan retrieved_contexts")

    run.status = RagRunStatus.RUNNING_RAGAS
    db.commit()
    eval_started_at = time.perf_counter()
    metrics = evaluate_iteration_with_ragas(
        question=sample.user_input,
        contexts=sample.retrieved_contexts or [],
        answer=sample.response or "",
        reference=sample.reference or "",
    )
    sample.faithfulness = metrics.get("faithfulness")
    sample.answer_relevancy = metrics.get("answer_relevancy")
    sample.context_precision = metrics.get("context_precision")
    sample.context_recall = metrics.get("context_recall")
    sample.evaluation_duration_seconds = time.perf_counter() - eval_started_at
    sample.status = RagSampleStatus.COMPLETED
    sample.completed_at = datetime.now(timezone.utc)
    db.commit()


def _update_progress(db, run_id: int) -> None:
    run = db.query(RagEvaluationRun).filter(RagEvaluationRun.id == run_id).first()
    samples = db.query(RagEvaluationSample).filter(RagEvaluationSample.run_id == run_id).all()
    aggregate = calculate_run_aggregate(samples)
    processed = sum(1 for sample in samples if sample.status in {RagSampleStatus.COMPLETED, RagSampleStatus.FAILED})
    run.processed_samples = processed
    run.successful_samples = aggregate.successful_samples
    run.failed_samples = aggregate.failed_samples
    run.progress = round((processed / run.total_samples) * 100, 2) if run.total_samples else 0.0
    db.commit()


def _finish_run(db, run_id: int) -> None:
    run = db.query(RagEvaluationRun).filter(RagEvaluationRun.id == run_id).first()
    run.status = RagRunStatus.AGGREGATING
    db.commit()
    samples = db.query(RagEvaluationSample).filter(RagEvaluationSample.run_id == run_id).order_by(RagEvaluationSample.sample_index.asc()).all()
    aggregate = calculate_run_aggregate(samples)
    run.successful_samples = aggregate.successful_samples
    run.failed_samples = aggregate.failed_samples
    run.processed_samples = aggregate.successful_samples + aggregate.failed_samples
    run.progress = 100.0 if run.total_samples else 0.0
    run.faithfulness_avg = aggregate.faithfulness_avg
    run.answer_relevancy_avg = aggregate.answer_relevancy_avg
    run.context_precision_avg = aggregate.context_precision_avg
    run.context_recall_avg = aggregate.context_recall_avg
    run.status = RagRunStatus.PARTIAL_FAILED if aggregate.failed_samples else RagRunStatus.COMPLETED
    run.completed_at = datetime.now(timezone.utc)
    db.commit()
    persist_result_artifact(db, run.id, samples)
