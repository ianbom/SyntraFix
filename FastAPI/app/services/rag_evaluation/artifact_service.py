import csv
from io import BytesIO, StringIO
from pathlib import Path
from typing import Iterable

from minio.error import S3Error
from sqlalchemy.orm import Session

from app.config import get_settings
from app.models.rag_evaluation import RagArtifactType, RagEvaluationArtifact, RagEvaluationSample
from app.services.minio import ensure_bucket_exists, get_minio_client

LOCAL_ARTIFACT_DIR = Path(__file__).resolve().parents[2] / "rag_evaluation_artifacts"


def save_bytes(filename: str, content: bytes, content_type: str = "text/csv") -> str:
    settings = get_settings()
    object_name = f"rag-evaluation/{filename}"
    try:
        client = get_minio_client()
        ensure_bucket_exists(client)
        client.put_object(
            settings.MINIO_BUCKET,
            object_name,
            BytesIO(content),
            length=len(content),
            content_type=content_type,
        )
        return object_name
    except Exception as error:
        if not isinstance(error, S3Error):
            print(f"Warning: MinIO artifact upload failed, using local storage: {error}")
        LOCAL_ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
        path = LOCAL_ARTIFACT_DIR / filename
        path.write_bytes(content)
        return str(path)


def create_result_csv(samples: Iterable[RagEvaluationSample]) -> bytes:
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(
        [
            "sample_index", "user_input", "response", "retrieved_contexts", "reference",
            "faithfulness", "answer_relevancy", "context_precision", "context_recall",
            "rag_duration_seconds", "evaluation_duration_seconds", "status", "error_message",
        ]
    )
    for sample in samples:
        writer.writerow(
            [
                sample.sample_index,
                sample.user_input,
                sample.response or "",
                sample.retrieved_contexts or [],
                sample.reference or "",
                _empty_none(sample.faithfulness),
                _empty_none(sample.answer_relevancy),
                _empty_none(sample.context_precision),
                _empty_none(sample.context_recall),
                _empty_none(sample.rag_duration_seconds),
                _empty_none(sample.evaluation_duration_seconds),
                getattr(sample.status, "value", sample.status),
                sample.error_message or "",
            ]
        )
    return output.getvalue().encode("utf-8")


def persist_result_artifact(db: Session, run_id: int, samples: Iterable[RagEvaluationSample]) -> RagEvaluationArtifact:
    filename = f"rag-evaluation-run-{run_id}-result.csv"
    file_path = save_bytes(filename, create_result_csv(samples), content_type="text/csv")
    artifact = RagEvaluationArtifact(
        run_id=run_id,
        artifact_type=RagArtifactType.RESULT_CSV,
        file_path=file_path,
        filename=filename,
    )
    db.add(artifact)
    db.commit()
    db.refresh(artifact)
    return artifact


def read_artifact_bytes(artifact: RagEvaluationArtifact) -> bytes:
    return read_stored_bytes(artifact.file_path)


def read_stored_bytes(file_path: str) -> bytes:
    path = Path(file_path)
    if path.exists():
        return path.read_bytes()

    settings = get_settings()
    client = get_minio_client()
    response = client.get_object(settings.MINIO_BUCKET, file_path)
    try:
        return response.read()
    finally:
        response.close()
        response.release_conn()


def _empty_none(value):
    return "" if value is None else value
