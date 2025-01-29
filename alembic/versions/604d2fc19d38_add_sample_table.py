"""add sample table

Revision ID: 604d2fc19d38
Revises: 
Create Date: 2025-01-29 19:01:33.411243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '604d2fc19d38'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('samples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_samples_id'), 'samples', ['id'], unique=False)
    op.create_index(op.f('ix_samples_name'), 'samples', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_samples_name'), table_name='samples')
    op.drop_index(op.f('ix_samples_id'), table_name='samples')
    op.drop_table('samples')
    # ### end Alembic commands ###
