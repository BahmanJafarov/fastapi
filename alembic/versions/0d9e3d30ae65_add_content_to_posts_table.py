"""add content to posts table

Revision ID: 0d9e3d30ae65
Revises: f8d763eb5ed3
Create Date: 2024-12-11 17:06:58.486713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d9e3d30ae65'
down_revision: Union[str, None] = 'f8d763eb5ed3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
