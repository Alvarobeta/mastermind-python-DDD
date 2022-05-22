"""deleted  multidimensional arrays from game

Revision ID: 514663984031
Revises: 9d09109f14be
Create Date: 2022-05-22 10:26:44.634507

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '514663984031'
down_revision = '9d09109f14be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'feedbacks')
    op.drop_column('games', 'attempts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('attempts', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('games', sa.Column('feedbacks', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
