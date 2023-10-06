"""updated user table columns

Revision ID: e4c651b15623
Revises: bd1f418bde1d
Create Date: 2023-10-06 10:22:22.692166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'e4c651b15623'
down_revision: Union[str, None] = 'bd1f418bde1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('mobile', sa.String(length=20), nullable=True))
    op.create_index(op.f('ix_users_mobile'), 'users', ['mobile'], unique=False)
    op.drop_column('users', 'deleted_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('deleted_at', mysql.DATETIME(), nullable=True))
    op.drop_index(op.f('ix_users_mobile'), table_name='users')
    op.drop_column('users', 'mobile')
    # ### end Alembic commands ###