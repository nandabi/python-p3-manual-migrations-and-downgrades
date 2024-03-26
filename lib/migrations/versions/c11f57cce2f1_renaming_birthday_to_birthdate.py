"""Renaming birthday to birthdate

Revision ID: c11f57cce2f1
Revises: cb8762fde176
Create Date: 2024-03-22 05:11:48.852139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c11f57cce2f1'
down_revision = 'cb8762fde176'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'birthday', new_column_name='birthdate')


def downgrade() -> None:
    op.alter_column('scholars', 'birthdate', new_column_name='birthday')