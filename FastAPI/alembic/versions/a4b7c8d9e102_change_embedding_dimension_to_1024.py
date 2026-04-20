"""change_embedding_dimension_to_1024

Revision ID: a4b7c8d9e102
Revises: f3a1d2c4b5e6
Create Date: 2026-04-20 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import pgvector.sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "a4b7c8d9e102"
down_revision: Union[str, None] = "f3a1d2c4b5e6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "document_chunks",
        "embedding",
        existing_type=pgvector.sqlalchemy.vector.VECTOR(dim=768),
        type_=pgvector.sqlalchemy.vector.VECTOR(dim=1024),
        existing_nullable=True,
    )
    op.alter_column(
        "document_chunks",
        "possibly_question_embedding",
        existing_type=pgvector.sqlalchemy.vector.VECTOR(dim=768),
        type_=pgvector.sqlalchemy.vector.VECTOR(dim=1024),
        existing_nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "document_chunks",
        "possibly_question_embedding",
        existing_type=pgvector.sqlalchemy.vector.VECTOR(dim=1024),
        type_=pgvector.sqlalchemy.vector.VECTOR(dim=768),
        existing_nullable=True,
    )
    op.alter_column(
        "document_chunks",
        "embedding",
        existing_type=pgvector.sqlalchemy.vector.VECTOR(dim=1024),
        type_=pgvector.sqlalchemy.vector.VECTOR(dim=768),
        existing_nullable=True,
    )
