"""add-notess-field

Revision ID: 123bd12b374c
Revises: 698f2f334f02
Create Date: 2019-04-10 17:27:50.387685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '123bd12b374c'
down_revision = '698f2f334f02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charge', sa.Column('notes', sa.String(), nullable=True))
    op.add_column('charge', sa.Column('please_expunge', sa.Boolean(), nullable=True))
    op.add_column('client', sa.Column('notes', sa.String(), nullable=True))
    op.add_column('conviction', sa.Column('notes', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conviction', 'notes')
    op.drop_column('client', 'notes')
    op.drop_column('charge', 'please_expunge')
    op.drop_column('charge', 'notes')
    # ### end Alembic commands ###