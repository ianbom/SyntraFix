"""add_processing_progress_to_documents

Revision ID: 9f2d4d2dc2d1
Revises: 8c5add0dd1a8
Create Date: 2026-04-13 10:45:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9f2d4d2dc2d1"
down_revision: Union[str, None] = "8c5add0dd1a8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "documents",
        sa.Column("processing_progress", sa.Integer(), nullable=False, server_default=sa.text("0")),
    )
    op.execute("UPDATE documents SET processing_progress = 100 WHERE processing_status = 'completed'")


def downgrade() -> None:
    op.drop_column("documents", "processing_progress")
