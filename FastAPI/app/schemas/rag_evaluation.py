from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

EvaluationMode = Literal["pipeline", "score_only"]
DatasetStatus = Literal["uploaded", "validating", "ready", "invalid"]
RunStatus = Literal[
    "queued", "preparing", "running_rag", "running_ragas", "aggregating",
    "completed", "partial_failed", "failed", "cancelled",
]
SampleStatus = Literal["pending", "processing", "completed", "failed"]


class RagDatasetRowResponse(BaseModel):
    id: int
    row_number: int
    test_case_id: str | None = None
    user_input: str
    reference: str | None = None
    response: str | None = None
    retrieved_contexts: list[str] | None = None
    category: str | None = None
    source_document_ids: list[Any] | None = None
    notes: str | None = None
    validation_status: str
    validation_message: str | None = None

    class Config:
        from_attributes = True


class RagDatasetResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    source_type: str
    evaluation_mode: EvaluationMode
    original_filename: str | None = None
    file_path: str | None = None
    dataset_hash: str | None = None
    total_rows: int
    valid_rows: int
    invalid_rows: int
    status: DatasetStatus
    validation_errors: list[dict[str, Any]] | None = None
    created_by: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True
        use_enum_values = True


class RagDatasetListResponse(BaseModel):
    datasets: list[RagDatasetResponse]
    total: int
    page: int
    per_page: int
    pages: int


class RagDatasetDetailResponse(RagDatasetResponse):
    rows: list[RagDatasetRowResponse] = []


class UpdateDatasetRowRequest(BaseModel):
    reference: str | None = None
    notes: str | None = None
    category: str | None = None


class CreateRunRequest(BaseModel):
    dataset_id: int
    name: str = Field(min_length=1)
    description: str | None = None
    evaluation_mode: EvaluationMode | None = None
    evaluator_model: str | None = None
    config: dict[str, Any] | None = None


class RagArtifactResponse(BaseModel):
    id: int
    artifact_type: str
    file_path: str
    filename: str
    created_at: datetime | None = None

    class Config:
        from_attributes = True
        use_enum_values = True


class RagRunResponse(BaseModel):
    id: int
    dataset_id: int
    dataset_name: str | None = None
    name: str
    description: str | None = None
    status: RunStatus
    evaluation_mode: EvaluationMode
    total_samples: int
    processed_samples: int
    successful_samples: int
    failed_samples: int
    progress: float
    faithfulness_avg: float | None = None
    answer_relevancy_avg: float | None = None
    context_precision_avg: float | None = None
    context_recall_avg: float | None = None
    generator_model: str | None = None
    embedding_model: str | None = None
    evaluator_model: str | None = None
    ragas_version: str | None = None
    config_snapshot: dict[str, Any] | None = None
    celery_task_id: str | None = None
    created_by: int
    started_at: datetime | None = None
    completed_at: datetime | None = None
    error_message: str | None = None
    created_at: datetime | None = None
    artifacts: list[RagArtifactResponse] = []

    class Config:
        from_attributes = True
        use_enum_values = True


class RagRunListResponse(BaseModel):
    runs: list[RagRunResponse]
    total: int
    page: int
    per_page: int
    pages: int


class RagSampleResponse(BaseModel):
    id: int
    run_id: int
    dataset_row_id: int
    sample_index: int
    user_input: str
    reference: str | None = None
    response: str | None = None
    retrieved_contexts: list[str] | None = None
    references_metadata: list[dict[str, Any]] | None = None
    faithfulness: float | None = None
    answer_relevancy: float | None = None
    context_precision: float | None = None
    context_recall: float | None = None
    rag_duration_seconds: float | None = None
    evaluation_duration_seconds: float | None = None
    status: SampleStatus
    error_message: str | None = None
    completed_at: datetime | None = None

    class Config:
        from_attributes = True
        use_enum_values = True


class RagSampleListResponse(BaseModel):
    samples: list[RagSampleResponse]
    total: int
    page: int
    per_page: int
    pages: int


class ChatExportRequest(BaseModel):
    date_from: datetime | None = None
    date_to: datetime | None = None
    user_ids: list[int] = []
    conversation_ids: list[int] = []
    only_with_references: bool = False
    create_dataset: bool = False
    name: str | None = None


class DashboardHistoryPoint(BaseModel):
    id: int
    name: str
    created_at: datetime | None = None
    total_samples: int
    faithfulness: float | None = None
    answer_relevancy: float | None = None
    context_precision: float | None = None
    context_recall: float | None = None


class RagDashboardSummaryResponse(BaseModel):
    active_run: RagRunResponse | None = None
    latest_completed_run: RagRunResponse | None = None
    previous_completed_run: RagRunResponse | None = None
    history: list[DashboardHistoryPoint]


class RagDashboardDistributionResponse(BaseModel):
    run_id: int | None = None
    buckets: dict[str, dict[str, int]]
