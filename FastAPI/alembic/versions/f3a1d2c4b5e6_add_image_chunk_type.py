"""add_image_chunk_type

Revision ID: f3a1d2c4b5e6
Revises: 9f2d4d2dc2d1
Create Date: 2026-04-13 15:00:00.000000

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "f3a1d2c4b5e6"
down_revision: Union[str, None] = "9f2d4d2dc2d1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE chunktype ADD VALUE IF NOT EXISTS 'IMAGE'")


def downgrade() -> None:
    # PostgreSQL enum values are append-only in-place; downgrade kept as no-op.
    pass
