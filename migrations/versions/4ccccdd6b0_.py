"""empty message

Revision ID: 4ccccdd6b0
Revises: 16d40b17caf
Create Date: 2015-12-03 14:04:34.407265

"""

# revision identifiers, used by Alembic.
revision = '4ccccdd6b0'
down_revision = '16d40b17caf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_installation', sa.Column('status_id', sa.Integer(), nullable=False))
    op.drop_column('app_installation', 'status')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_installation', sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('app_installation', 'status_id')
    ### end Alembic commands ###
