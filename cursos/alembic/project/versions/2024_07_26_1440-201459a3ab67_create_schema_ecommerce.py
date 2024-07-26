"""create schema ecommerce

Revision ID: 201459a3ab67
Revises: 
Create Date: 2024-07-26 14:40:13.805576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '201459a3ab67'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE SCHEMA IF NOT EXISTS ecommerce_olist;')


def downgrade() -> None:
    op.execute('DROP SCHEMA IF EXISTS ecommerce_olist CASCADE;')
