"""add_rag_evaluation_tables

Revision ID: b7c2d4e6f801
Revises: a4b7c8d9e102
Create Date: 2026-06-21 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "b7c2d4e6f801"
down_revision: Union[str, None] = "a4b7c8d9e102"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    evaluation_mode = postgresql.ENUM("PIPELINE", "SCORE_ONLY", name="ragevaluationmode", create_type=False)
    source_type = postgresql.ENUM("CSV_UPLOAD", "CHAT_EXPORT", name="ragdatasetsourcetype", create_type=False)
    dataset_status = postgresql.ENUM("UPLOADED", "VALIDATING", "READY", "INVALID", name="ragdatasetstatus", create_type=False)
    run_status = postgresql.ENUM(
        "QUEUED", "PREPARING", "RUNNING_RAG", "RUNNING_RAGAS", "AGGREGATING",
        "COMPLETED", "PARTIAL_FAILED", "FAILED", "CANCELLED", name="ragrunstatus", create_type=False,
    )
    sample_status = postgresql.ENUM("PENDING", "PROCESSING", "COMPLETED", "FAILED", name="ragsamplestatus", create_type=False)
    artifact_type = postgresql.ENUM("INPUT_CSV", "RESULT_CSV", "ERROR_CSV", "CONFIG_JSON", name="ragartifacttype", create_type=False)

    bind = op.get_bind()
    for enum_type in (evaluation_mode, source_type, dataset_status, run_status, sample_status, artifact_type):
        enum_type.create(bind, checkfirst=True)

    op.create_table(
        "rag_evaluation_datasets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("source_type", source_type, nullable=False),
        sa.Column("evaluation_mode", evaluation_mode, nullable=False),
        sa.Column("original_filename", sa.String(length=255), nullable=True),
        sa.Column("file_path", sa.Text(), nullable=True),
        sa.Column("dataset_hash", sa.String(length=64), nullable=True),
        sa.Column("total_rows", sa.Integer(), nullable=True),
        sa.Column("valid_rows", sa.Integer(), nullable=True),
        sa.Column("invalid_rows", sa.Integer(), nullable=True),
        sa.Column("status", dataset_status, nullable=False),
        sa.Column("validation_errors", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["created_by"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_rag_evaluation_datasets_id"), "rag_evaluation_datasets", ["id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_datasets_dataset_hash"), "rag_evaluation_datasets", ["dataset_hash"], unique=False)

    op.create_table(
        "rag_evaluation_dataset_rows",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dataset_id", sa.Integer(), nullable=False),
        sa.Column("row_number", sa.Integer(), nullable=False),
        sa.Column("test_case_id", sa.String(length=255), nullable=True),
        sa.Column("user_input", sa.Text(), nullable=False),
        sa.Column("reference", sa.Text(), nullable=True),
        sa.Column("response", sa.Text(), nullable=True),
        sa.Column("retrieved_contexts", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("category", sa.String(length=255), nullable=True),
        sa.Column("source_document_ids", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("validation_status", sa.String(length=20), nullable=False),
        sa.Column("validation_message", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["dataset_id"], ["rag_evaluation_datasets.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_rag_evaluation_dataset_rows_id"), "rag_evaluation_dataset_rows", ["id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_dataset_rows_dataset_id"), "rag_evaluation_dataset_rows", ["dataset_id"], unique=False)

    op.create_table(
        "rag_evaluation_runs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dataset_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("status", run_status, nullable=False),
        sa.Column("evaluation_mode", evaluation_mode, nullable=False),
        sa.Column("total_samples", sa.Integer(), nullable=True),
        sa.Column("processed_samples", sa.Integer(), nullable=True),
        sa.Column("successful_samples", sa.Integer(), nullable=True),
        sa.Column("failed_samples", sa.Integer(), nullable=True),
        sa.Column("progress", sa.Float(), nullable=True),
        sa.Column("faithfulness_avg", sa.Float(), nullable=True),
        sa.Column("answer_relevancy_avg", sa.Float(), nullable=True),
        sa.Column("context_precision_avg", sa.Float(), nullable=True),
        sa.Column("context_recall_avg", sa.Float(), nullable=True),
        sa.Column("generator_model", sa.String(length=255), nullable=True),
        sa.Column("embedding_model", sa.String(length=255), nullable=True),
        sa.Column("evaluator_model", sa.String(length=255), nullable=True),
        sa.Column("ragas_version", sa.String(length=80), nullable=True),
        sa.Column("config_snapshot", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("celery_task_id", sa.String(length=255), nullable=True),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["created_by"], ["users.id"]),
        sa.ForeignKeyConstraint(["dataset_id"], ["rag_evaluation_datasets.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_rag_evaluation_runs_id"), "rag_evaluation_runs", ["id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_runs_dataset_id"), "rag_evaluation_runs", ["dataset_id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_runs_status"), "rag_evaluation_runs", ["status"], unique=False)

    op.create_table(
        "rag_evaluation_samples",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("run_id", sa.Integer(), nullable=False),
        sa.Column("dataset_row_id", sa.Integer(), nullable=False),
        sa.Column("sample_index", sa.Integer(), nullable=False),
        sa.Column("user_input", sa.Text(), nullable=False),
        sa.Column("reference", sa.Text(), nullable=True),
        sa.Column("response", sa.Text(), nullable=True),
        sa.Column("retrieved_contexts", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("references_metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("faithfulness", sa.Float(), nullable=True),
        sa.Column("answer_relevancy", sa.Float(), nullable=True),
        sa.Column("context_precision", sa.Float(), nullable=True),
        sa.Column("context_recall", sa.Float(), nullable=True),
        sa.Column("rag_duration_seconds", sa.Float(), nullable=True),
        sa.Column("evaluation_duration_seconds", sa.Float(), nullable=True),
        sa.Column("status", sample_status, nullable=False),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["dataset_row_id"], ["rag_evaluation_dataset_rows.id"]),
        sa.ForeignKeyConstraint(["run_id"], ["rag_evaluation_runs.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_rag_evaluation_samples_id"), "rag_evaluation_samples", ["id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_samples_run_id"), "rag_evaluation_samples", ["run_id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_samples_dataset_row_id"), "rag_evaluation_samples", ["dataset_row_id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_samples_status"), "rag_evaluation_samples", ["status"], unique=False)

    op.create_table(
        "rag_evaluation_artifacts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("run_id", sa.Integer(), nullable=False),
        sa.Column("artifact_type", artifact_type, nullable=False),
        sa.Column("file_path", sa.Text(), nullable=False),
        sa.Column("filename", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["run_id"], ["rag_evaluation_runs.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_rag_evaluation_artifacts_id"), "rag_evaluation_artifacts", ["id"], unique=False)
    op.create_index(op.f("ix_rag_evaluation_artifacts_run_id"), "rag_evaluation_artifacts", ["run_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_rag_evaluation_artifacts_run_id"), table_name="rag_evaluation_artifacts")
    op.drop_index(op.f("ix_rag_evaluation_artifacts_id"), table_name="rag_evaluation_artifacts")
    op.drop_table("rag_evaluation_artifacts")
    op.drop_index(op.f("ix_rag_evaluation_samples_status"), table_name="rag_evaluation_samples")
    op.drop_index(op.f("ix_rag_evaluation_samples_dataset_row_id"), table_name="rag_evaluation_samples")
    op.drop_index(op.f("ix_rag_evaluation_samples_run_id"), table_name="rag_evaluation_samples")
    op.drop_index(op.f("ix_rag_evaluation_samples_id"), table_name="rag_evaluation_samples")
    op.drop_table("rag_evaluation_samples")
    op.drop_index(op.f("ix_rag_evaluation_runs_status"), table_name="rag_evaluation_runs")
    op.drop_index(op.f("ix_rag_evaluation_runs_dataset_id"), table_name="rag_evaluation_runs")
    op.drop_index(op.f("ix_rag_evaluation_runs_id"), table_name="rag_evaluation_runs")
    op.drop_table("rag_evaluation_runs")
    op.drop_index(op.f("ix_rag_evaluation_dataset_rows_dataset_id"), table_name="rag_evaluation_dataset_rows")
    op.drop_index(op.f("ix_rag_evaluation_dataset_rows_id"), table_name="rag_evaluation_dataset_rows")
    op.drop_table("rag_evaluation_dataset_rows")
    op.drop_index(op.f("ix_rag_evaluation_datasets_dataset_hash"), table_name="rag_evaluation_datasets")
    op.drop_index(op.f("ix_rag_evaluation_datasets_id"), table_name="rag_evaluation_datasets")
    op.drop_table("rag_evaluation_datasets")

    bind = op.get_bind()
    for name in (
        "ragartifacttype", "ragsamplestatus", "ragrunstatus",
        "ragdatasetstatus", "ragdatasetsourcetype", "ragevaluationmode",
    ):
        postgresql.ENUM(name=name).drop(bind, checkfirst=True)
