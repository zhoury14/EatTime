"""init migration

Revision ID: f65533a766d1
Revises: 3f059b33aaea
Create Date: 2016-07-13 01:47:50.786000

"""

# revision identifiers, used by Alembic.
revision = 'f65533a766d1'
down_revision = '3f059b33aaea'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customerusers', sa.Column('altitude', sa.Float(), nullable=True))
    op.add_column('customerusers', sa.Column('logitude', sa.Float(), nullable=True))
    op.add_column('users', sa.Column('altitude', sa.Float(), nullable=True))
    op.add_column('users', sa.Column('logitude', sa.Float(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'logitude')
    op.drop_column('users', 'altitude')
    op.drop_column('customerusers', 'logitude')
    op.drop_column('customerusers', 'altitude')
    ### end Alembic commands ###
