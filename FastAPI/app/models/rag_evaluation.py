import enum

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class RagEvaluationMode(str, enum.Enum):
    PIPELINE = "pipeline"
    SCORE_ONLY = "score_only"


class RagDatasetSourceType(str, enum.Enum):
    CSV_UPLOAD = "csv_upload"
    CHAT_EXPORT = "chat_export"


class RagDatasetStatus(str, enum.Enum):
    UPLOADED = "uploaded"
    VALIDATING = "validating"
    READY = "ready"
    INVALID = "invalid"


class RagRunStatus(str, enum.Enum):
    QUEUED = "queued"
    PREPARING = "preparing"
    RUNNING_RAG = "running_rag"
    RUNNING_RAGAS = "running_ragas"
    AGGREGATING = "aggregating"
    COMPLETED = "completed"
    PARTIAL_FAILED = "partial_failed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class RagSampleStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class RagArtifactType(str, enum.Enum):
    INPUT_CSV = "input_csv"
    RESULT_CSV = "result_csv"
    ERROR_CSV = "error_csv"
    CONFIG_JSON = "config_json"


class RagEvaluationDataset(Base):
    __tablename__ = "rag_evaluation_datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    source_type = Column(Enum(RagDatasetSourceType), nullable=False, default=RagDatasetSourceType.CSV_UPLOAD)
    evaluation_mode = Column(Enum(RagEvaluationMode), nullable=False)
    original_filename = Column(String(255))
    file_path = Column(Text)
    dataset_hash = Column(String(64), index=True)
    total_rows = Column(Integer, default=0)
    valid_rows = Column(Integer, default=0)
    invalid_rows = Column(Integer, default=0)
    status = Column(Enum(RagDatasetStatus), nullable=False, default=RagDatasetStatus.UPLOADED)
    validation_errors = Column(JSONB)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    rows = relationship("RagEvaluationDatasetRow", back_populates="dataset", cascade="all, delete-orphan")
    runs = relationship("RagEvaluationRun", back_populates="dataset")


class RagEvaluationDatasetRow(Base):
    __tablename__ = "rag_evaluation_dataset_rows"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("rag_evaluation_datasets.id", ondelete="CASCADE"), nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    test_case_id = Column(String(255))
    user_input = Column(Text, nullable=False)
    reference = Column(Text)
    response = Column(Text)
    retrieved_contexts = Column(JSONB)
    category = Column(String(255))
    source_document_ids = Column(JSONB)
    notes = Column(Text)
    validation_status = Column(String(20), nullable=False)
    validation_message = Column(Text)

    dataset = relationship("RagEvaluationDataset", back_populates="rows")
    samples = relationship("RagEvaluationSample", back_populates="dataset_row")


class RagEvaluationRun(Base):
    __tablename__ = "rag_evaluation_runs"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("rag_evaluation_datasets.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(Enum(RagRunStatus), nullable=False, default=RagRunStatus.QUEUED, index=True)
    evaluation_mode = Column(Enum(RagEvaluationMode), nullable=False)
    total_samples = Column(Integer, default=0)
    processed_samples = Column(Integer, default=0)
    successful_samples = Column(Integer, default=0)
    failed_samples = Column(Integer, default=0)
    progress = Column(Float, default=0.0)
    faithfulness_avg = Column(Float)
    answer_relevancy_avg = Column(Float)
    context_precision_avg = Column(Float)
    context_recall_avg = Column(Float)
    generator_model = Column(String(255))
    embedding_model = Column(String(255))
    evaluator_model = Column(String(255))
    ragas_version = Column(String(80))
    config_snapshot = Column(JSONB)
    celery_task_id = Column(String(255))
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    error_message = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    dataset = relationship("RagEvaluationDataset", back_populates="runs")
    samples = relationship("RagEvaluationSample", back_populates="run", cascade="all, delete-orphan")
    artifacts = relationship("RagEvaluationArtifact", back_populates="run", cascade="all, delete-orphan")


class RagEvaluationSample(Base):
    __tablename__ = "rag_evaluation_samples"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("rag_evaluation_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    dataset_row_id = Column(Integer, ForeignKey("rag_evaluation_dataset_rows.id"), nullable=False, index=True)
    sample_index = Column(Integer, nullable=False)
    user_input = Column(Text, nullable=False)
    reference = Column(Text)
    response = Column(Text)
    retrieved_contexts = Column(JSONB)
    references_metadata = Column(JSONB)
    faithfulness = Column(Float)
    answer_relevancy = Column(Float)
    context_precision = Column(Float)
    context_recall = Column(Float)
    rag_duration_seconds = Column(Float)
    evaluation_duration_seconds = Column(Float)
    status = Column(Enum(RagSampleStatus), nullable=False, default=RagSampleStatus.PENDING, index=True)
    error_message = Column(Text)
    completed_at = Column(DateTime(timezone=True))

    run = relationship("RagEvaluationRun", back_populates="samples")
    dataset_row = relationship("RagEvaluationDatasetRow", back_populates="samples")


class RagEvaluationArtifact(Base):
    __tablename__ = "rag_evaluation_artifacts"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("rag_evaluation_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    artifact_type = Column(Enum(RagArtifactType), nullable=False)
    file_path = Column(Text, nullable=False)
    filename = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    run = relationship("RagEvaluationRun", back_populates="artifacts")
