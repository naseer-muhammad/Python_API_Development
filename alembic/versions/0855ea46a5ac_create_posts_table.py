"""create posts table

Revision ID: 0855ea46a5ac
Revises: 
Create Date: 2025-11-13 10:46:21.431288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0855ea46a5ac'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.create_table("posts", 
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_table("posts")
    pass
