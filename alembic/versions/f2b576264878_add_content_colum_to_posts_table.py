"""add content colum to posts table

Revision ID: f2b576264878
Revises: 0855ea46a5ac
Create Date: 2025-11-13 11:27:17.961850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2b576264878'
down_revision: Union[str, Sequence[str], None] = '0855ea46a5ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
