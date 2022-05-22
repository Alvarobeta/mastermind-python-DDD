"""added json attempts

Revision ID: 00f39c918a98
Revises: 514663984031
Create Date: 2022-05-22 10:42:35.213945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00f39c918a98'
down_revision = '514663984031'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('attempts', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'attempts')
    # ### end Alembic commands ###