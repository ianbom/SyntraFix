import hashlib
from typing import Any

from fastapi import HTTPException, UploadFile
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.rag_evaluation import (
    RagDatasetSourceType,
    RagDatasetStatus,
    RagEvaluationDataset,
    RagEvaluationDatasetRow,
    RagEvaluationMode,
    RagEvaluationSample,
)
from app.services.rag_evaluation.artifact_service import save_bytes
from app.services.rag_evaluation.csv_validator import read_csv_text, validate_csv_rows


async def create_dataset_from_upload(
    db: Session,
    file: UploadFile,
    evaluation_mode: str,
    created_by: int,
    name: str | None = None,
    description: str | None = None,
    source_type: RagDatasetSourceType = RagDatasetSourceType.CSV_UPLOAD,
) -> RagEvaluationDataset:
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="File harus berformat .csv")

    content = await file.read()
    return create_dataset_from_csv_bytes(
        db=db,
        content=content,
        filename=file.filename,
        evaluation_mode=evaluation_mode,
        created_by=created_by,
        name=name or file.filename.rsplit(".", 1)[0],
        description=description,
        source_type=source_type,
    )


def create_dataset_from_csv_bytes(
    db: Session,
    content: bytes,
    filename: str,
    evaluation_mode: str,
    created_by: int,
    name: str,
    description: str | None = None,
    source_type: RagDatasetSourceType = RagDatasetSourceType.CSV_UPLOAD,
) -> RagEvaluationDataset:
    mode = _mode(evaluation_mode)
    try:
        raw_rows = read_csv_text(content)
        validation = validate_csv_rows(raw_rows, evaluation_mode=mode.value)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    dataset_hash = hashlib.sha256(content).hexdigest()
    file_path = save_bytes(f"dataset-{dataset_hash[:12]}-{filename}", content, content_type="text/csv")
    dataset = RagEvaluationDataset(
        name=name,
        description=description,
        source_type=source_type,
        evaluation_mode=mode,
        original_filename=filename,
        file_path=file_path,
        dataset_hash=dataset_hash,
        total_rows=validation.total_rows,
        valid_rows=validation.valid_rows,
        invalid_rows=validation.invalid_rows,
        status=RagDatasetStatus.READY if validation.invalid_rows == 0 else RagDatasetStatus.INVALID,
        validation_errors=validation.errors,
        created_by=created_by,
    )
    db.add(dataset)
    db.flush()

    for row in validation.rows:
        db.add(
            RagEvaluationDatasetRow(
                dataset_id=dataset.id,
                row_number=row.row_number,
                test_case_id=row.test_case_id,
                user_input=row.user_input,
                reference=row.reference,
                response=row.response,
                retrieved_contexts=row.retrieved_contexts,
                category=row.category,
                source_document_ids=row.source_document_ids,
                notes=row.notes,
                validation_status=row.validation_status,
                validation_message=row.validation_message,
            )
        )

    db.commit()
    db.refresh(dataset)
    return dataset


def list_datasets(db: Session, page: int, per_page: int) -> tuple[list[RagEvaluationDataset], int]:
    query = db.query(RagEvaluationDataset).order_by(desc(RagEvaluationDataset.created_at), desc(RagEvaluationDataset.id))
    total = query.count()
    datasets = query.offset((page - 1) * per_page).limit(per_page).all()
    return datasets, total


def get_dataset_or_404(db: Session, dataset_id: int) -> RagEvaluationDataset:
    dataset = db.query(RagEvaluationDataset).filter(RagEvaluationDataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset evaluasi tidak ditemukan")
    return dataset


def get_dataset_rows(db: Session, dataset_id: int, page: int, per_page: int) -> tuple[list[RagEvaluationDatasetRow], int]:
    get_dataset_or_404(db, dataset_id)
    query = db.query(RagEvaluationDatasetRow).filter(RagEvaluationDatasetRow.dataset_id == dataset_id).order_by(RagEvaluationDatasetRow.row_number.asc())
    total = query.count()
    rows = query.offset((page - 1) * per_page).limit(per_page).all()
    return rows, total


def update_dataset_row(db: Session, dataset_id: int, row_id: int, values: dict[str, Any]) -> RagEvaluationDatasetRow:
    row = db.query(RagEvaluationDatasetRow).filter(
        RagEvaluationDatasetRow.dataset_id == dataset_id,
        RagEvaluationDatasetRow.id == row_id,
    ).first()
    if not row:
        raise HTTPException(status_code=404, detail="Baris dataset tidak ditemukan")

    for field in ("reference", "notes", "category"):
        if field in values:
            setattr(row, field, values[field])

    if row.user_input.strip() and row.reference and row.reference.strip():
        row.validation_status = "valid"
        row.validation_message = None
    else:
        row.validation_status = "invalid"
        row.validation_message = "user_input dan reference wajib diisi"

    _refresh_dataset_counts(db, dataset_id)
    db.commit()
    db.refresh(row)
    return row


def delete_dataset_row(db: Session, dataset_id: int, row_id: int) -> None:
    row = db.query(RagEvaluationDatasetRow).filter(
        RagEvaluationDatasetRow.dataset_id == dataset_id,
        RagEvaluationDatasetRow.id == row_id,
    ).first()
    if not row:
        raise HTTPException(status_code=404, detail="Baris dataset tidak ditemukan")

    linked_samples = db.query(RagEvaluationSample).filter(RagEvaluationSample.dataset_row_id == row_id).count()
    if linked_samples:
        raise HTTPException(status_code=400, detail="Baris dataset sudah digunakan pada hasil evaluasi")

    db.delete(row)
    db.flush()
    _refresh_dataset_counts(db, dataset_id)
    db.commit()

def delete_dataset(db: Session, dataset_id: int) -> None:
    dataset = get_dataset_or_404(db, dataset_id)
    db.delete(dataset)
    db.commit()


def _refresh_dataset_counts(db: Session, dataset_id: int) -> None:
    dataset = get_dataset_or_404(db, dataset_id)
    rows = db.query(RagEvaluationDatasetRow).filter(RagEvaluationDatasetRow.dataset_id == dataset_id).all()
    valid_rows = sum(1 for row in rows if row.validation_status == "valid")
    dataset.total_rows = len(rows)
    dataset.valid_rows = valid_rows
    dataset.invalid_rows = len(rows) - valid_rows
    dataset.status = RagDatasetStatus.READY if dataset.invalid_rows == 0 else RagDatasetStatus.INVALID
    dataset.validation_errors = [
        {"row_number": row.row_number, "message": row.validation_message}
        for row in rows
        if row.validation_status == "invalid"
    ]


def _mode(value: str) -> RagEvaluationMode:
    try:
        return RagEvaluationMode(value)
    except ValueError as error:
        raise HTTPException(status_code=400, detail="Mode evaluasi harus pipeline atau score_only") from error
