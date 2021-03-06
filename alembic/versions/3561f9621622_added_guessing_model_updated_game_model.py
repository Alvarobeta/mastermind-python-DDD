"""added guessing model, updated game model

Revision ID: 3561f9621622
Revises: bd49d0a91d66
Create Date: 2022-05-21 11:03:28.254337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3561f9621622'
down_revision = 'bd49d0a91d66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guessings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guessings_id'), 'guessings', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_guessings_id'), table_name='guessings')
    op.drop_table('guessings')
    # ### end Alembic commands ###
