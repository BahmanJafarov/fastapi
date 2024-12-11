"""add user table

Revision ID: 58c66d8caeb3
Revises: 57816c27d7e3
Create Date: 2024-12-11 17:19:21.342226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58c66d8caeb3'
down_revision: Union[str, None] = '57816c27d7e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
