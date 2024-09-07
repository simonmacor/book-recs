"""create users, books and preferences tables

Revision ID: c3393229da11
Revises: 
Create Date: 2024-09-04 21:25:09.301571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3393229da11'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(100), nullable=False),
        sa.Column('email', sa.String(255)),
    )

    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('author', sa.String(200), nullable=False),
        sa.Column('theme', sa.String(200), nullable=False),
        sa.Column('period', sa.String(200), nullable=False),
        sa.Column('style', sa.String(200), nullable=False),
    )

    op.create_table(
        'preferences',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column('theme', sa.String(200), nullable=False),
        sa.Column('period', sa.String(200), nullable=False),
        sa.Column('style', sa.String(200), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('books')
    op.drop_table('preferences')
