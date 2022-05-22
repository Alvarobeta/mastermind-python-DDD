"""delete attempts

Revision ID: 2487e2b66cd7
Revises: 4c14320e2c3f
Create Date: 2022-05-21 21:21:53.299468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2487e2b66cd7'
down_revision = '4c14320e2c3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'attempts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('attempts', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###