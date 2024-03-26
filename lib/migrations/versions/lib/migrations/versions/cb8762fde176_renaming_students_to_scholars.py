"""Renaming students to scholars

Revision ID: cb8762fde176
Revises: 791279dd0760
Create Date: 2024-03-22 05:01:41.489309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb8762fde176'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')