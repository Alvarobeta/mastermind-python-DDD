"""deleted Game model added pivot class

Revision ID: 17059890b0f1
Revises: 2efe9e27698c
Create Date: 2022-05-21 23:12:41.261881

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '17059890b0f1'
down_revision = '2efe9e27698c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todelete',
    sa.Column('id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todelete_id'), 'todelete', ['id'], unique=False)
    op.drop_index('ix_games_id', table_name='games')
    op.drop_table('games')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('code', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('PLAYING', 'WON', 'LOST', name='game_status'), autoincrement=False, nullable=True),
    sa.Column('feedbacks', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.Column('attempts', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='games_pkey')
    )
    op.create_index('ix_games_id', 'games', ['id'], unique=False)
    op.drop_index(op.f('ix_todelete_id'), table_name='todelete')
    op.drop_table('todelete')
    # ### end Alembic commands ###