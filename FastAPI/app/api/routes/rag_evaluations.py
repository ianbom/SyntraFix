from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, Query, UploadFile
from fastapi.responses import Response

from app.api.deps import AdminUser, DBSession, require_admin_user
from app.schemas.rag_evaluation import (
    ChatExportRequest,
    CreateRunRequest,
    RagDashboardDistributionResponse,
    RagDashboardSummaryResponse,
    RagDatasetDetailResponse,
    RagDatasetListResponse,
    RagDatasetResponse,
    RagDatasetRowResponse,
    RagRunListResponse,
    RagRunResponse,
    RagSampleListResponse,
    UpdateDatasetRowRequest,
)
from app.services.rag_evaluation import dataset_service, evaluation_service
from app.services.rag_evaluation.artifact_service import read_artifact_bytes, read_stored_bytes
from app.services.rag_evaluation.chat_exporter import export_chat_csv

router = APIRouter(
    prefix="/rag-evaluation",
    tags=["RAG Evaluation"],
    dependencies=[Depends(require_admin_user)],
)


@router.post("/datasets/upload", response_model=RagDatasetDetailResponse)
async def upload_dataset(
    current_user: AdminUser,
    db: DBSession,
    file: Annotated[UploadFile, File()],
    evaluation_mode: Annotated[str, Form()] = "score_only",
    name: Annotated[str | None, Form()] = None,
    description: Annotated[str | None, Form()] = None,
):
    dataset = await dataset_service.create_dataset_from_upload(
        db=db,
        file=file,
        evaluation_mode=evaluation_mode,
        created_by=current_user.id,
        name=name,
        description=description,
    )
    return dataset


@router.get("/datasets", response_model=RagDatasetListResponse)
def list_datasets(
    db: DBSession,
    page: Annotated[int, Query(ge=1)] = 1,
    per_page: Annotated[int, Query(ge=1, le=100)] = 20,
):
    datasets, total = dataset_service.list_datasets(db, page=page, per_page=per_page)
    return {"datasets": datasets, "total": total, "page": page, "per_page": per_page, "pages": evaluation_service.pages(total, per_page)}


@router.get("/datasets/template")
def download_template():
    content = "user_input,response,retrieved_contexts,reference\n"
    filename = "rag-evaluation-score-only-template.csv"
    return Response(
        content=content.encode("utf-8"),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.get("/datasets/{dataset_id}", response_model=RagDatasetDetailResponse)
def get_dataset(dataset_id: int, db: DBSession):
    return dataset_service.get_dataset_or_404(db, dataset_id)


@router.get("/datasets/{dataset_id}/rows")
def get_dataset_rows(
    dataset_id: int,
    db: DBSession,
    page: Annotated[int, Query(ge=1)] = 1,
    per_page: Annotated[int, Query(ge=1, le=200)] = 50,
):
    rows, total = dataset_service.get_dataset_rows(db, dataset_id, page=page, per_page=per_page)
    return {"rows": rows, "total": total, "page": page, "per_page": per_page, "pages": evaluation_service.pages(total, per_page)}


@router.patch("/datasets/{dataset_id}/rows/{row_id}", response_model=RagDatasetRowResponse)
def update_dataset_row(dataset_id: int, row_id: int, request: UpdateDatasetRowRequest, db: DBSession):
    return dataset_service.update_dataset_row(db, dataset_id, row_id, request.model_dump(exclude_unset=True))


@router.delete("/datasets/{dataset_id}/rows/{row_id}")
def delete_dataset_row(dataset_id: int, row_id: int, db: DBSession):
    dataset_service.delete_dataset_row(db, dataset_id, row_id)
    return {"message": "Baris dataset dihapus"}

@router.delete("/datasets/{dataset_id}")
def delete_dataset(dataset_id: int, db: DBSession):
    dataset_service.delete_dataset(db, dataset_id)
    return {"message": "Dataset evaluasi dihapus"}


@router.get("/datasets/{dataset_id}/download")
def download_dataset(dataset_id: int, db: DBSession):
    dataset = dataset_service.get_dataset_or_404(db, dataset_id)
    content = read_stored_bytes(dataset.file_path)
    filename = dataset.original_filename or f"dataset-{dataset.id}.csv"
    return Response(
        content=content,
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.post("/chat-export")
def chat_export(request: ChatExportRequest, current_user: AdminUser, db: DBSession):
    content = export_chat_csv(
        db,
        user_ids=request.user_ids or None,
        conversation_ids=request.conversation_ids or None,
        only_with_references=request.only_with_references,
        date_from=request.date_from,
        date_to=request.date_to,
    )
    if request.create_dataset:
        dataset = dataset_service.create_dataset_from_csv_bytes(
            db=db,
            content=content,
            filename="chat-export-ragas.csv",
            evaluation_mode="score_only",
            created_by=current_user.id,
            name=request.name or "Chat Export RAG Dataset",
            description="Dataset draft dari export chat.",
        )
        return RagDatasetResponse.model_validate(dataset)
    return Response(
        content=content,
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="chat-export-ragas.csv"'},
    )


@router.post("/runs", response_model=RagRunResponse)
def create_run(request: CreateRunRequest, current_user: AdminUser, db: DBSession):
    run = evaluation_service.create_run(
        db=db,
        dataset_id=request.dataset_id,
        created_by=current_user.id,
        name=request.name,
        description=request.description,
        evaluation_mode=request.evaluation_mode,
        evaluator_model=request.evaluator_model,
        config=request.config,
    )
    return evaluation_service.to_run_dict(run)


@router.get("/runs", response_model=RagRunListResponse)
def list_runs(
    db: DBSession,
    page: Annotated[int, Query(ge=1)] = 1,
    per_page: Annotated[int, Query(ge=1, le=100)] = 20,
    status: Annotated[str | None, Query()] = None,
    dataset_id: Annotated[int | None, Query()] = None,
):
    runs, total = evaluation_service.list_runs(db, page=page, per_page=per_page, status=status, dataset_id=dataset_id)
    return {"runs": [evaluation_service.to_run_dict(run) for run in runs], "total": total, "page": page, "per_page": per_page, "pages": evaluation_service.pages(total, per_page)}


@router.get("/runs/latest", response_model=RagRunResponse | None)
def latest_run(db: DBSession):
    run = evaluation_service.get_latest_completed_run(db)
    return evaluation_service.to_run_dict(run) if run else None


@router.get("/runs/active", response_model=RagRunResponse | None)
def active_run(db: DBSession):
    run = evaluation_service.get_active_run(db)
    return evaluation_service.to_run_dict(run) if run else None


@router.get("/runs/{run_id}", response_model=RagRunResponse)
def get_run(run_id: int, db: DBSession):
    return evaluation_service.to_run_dict(evaluation_service.get_run_or_404(db, run_id))


@router.get("/runs/{run_id}/samples", response_model=RagSampleListResponse)
def get_run_samples(
    run_id: int,
    db: DBSession,
    page: Annotated[int, Query(ge=1)] = 1,
    per_page: Annotated[int, Query(ge=1, le=200)] = 50,
    status: Annotated[str | None, Query()] = None,
    all_rows: Annotated[bool, Query(alias="all")] = False,
):
    samples, total = evaluation_service.list_samples(db, run_id=run_id, page=page, per_page=per_page, status=status, all_rows=all_rows)
    response_per_page = total if all_rows and total else per_page
    return {"samples": samples, "total": total, "page": page, "per_page": response_per_page, "pages": evaluation_service.pages(total, response_per_page)}


@router.post("/runs/{run_id}/cancel", response_model=RagRunResponse)
def cancel_run(run_id: int, db: DBSession):
    return evaluation_service.to_run_dict(evaluation_service.cancel_run(db, run_id))


@router.get("/runs/{run_id}/export")
def export_run_result(run_id: int, db: DBSession):
    artifact = evaluation_service.get_result_artifact(db, run_id)
    return Response(
        content=read_artifact_bytes(artifact),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{artifact.filename}"'},
    )


@router.get("/dashboard/summary", response_model=RagDashboardSummaryResponse)
def dashboard_summary(db: DBSession):
    return evaluation_service.dashboard_summary(db)


@router.get("/dashboard/history")
def dashboard_history(db: DBSession):
    return evaluation_service.dashboard_summary(db)["history"]


@router.get("/dashboard/distribution", response_model=RagDashboardDistributionResponse)
def dashboard_distribution(db: DBSession, run_id: Annotated[int | None, Query()] = None):
    return evaluation_service.latest_distribution(db, run_id=run_id)
