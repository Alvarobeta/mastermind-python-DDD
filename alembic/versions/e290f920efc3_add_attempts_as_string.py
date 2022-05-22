"""add attempts as string

Revision ID: e290f920efc3
Revises: 49c7dd1c4262
Create Date: 2022-05-22 11:46:28.268377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e290f920efc3'
down_revision = '49c7dd1c4262'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('attempts', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'attempts')
    # ### end Alembic commands ###
