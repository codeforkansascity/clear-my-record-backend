"""changed string fields to all have explicit length

Revision ID: 087b9165b46a
Revises: 
Create Date: 2019-04-21 01:11:37.859664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '087b9165b46a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qualifying__question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('help_text', sa.Text(), nullable=True),
    sa.Column('disqualifying_answer', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('pw_hash', sa.String(length=128), nullable=True),
    sa.Column('user_type', sa.String(length=64), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=12), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('sex', sa.String(length=16), nullable=True),
    sa.Column('race', sa.String(length=64), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('address_line_1', sa.String(length=64), nullable=True),
    sa.Column('address_line_2', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('zip_code', sa.VARCHAR(length=10), nullable=True),
    sa.Column('license_number', sa.String(length=64), nullable=True),
    sa.Column('license_issuing_state', sa.VARCHAR(length=2), nullable=True),
    sa.Column('license_expiration_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('filing_court', sa.String(length=64), nullable=True),
    sa.Column('judicial_circuit_number', sa.Text(), nullable=True),
    sa.Column('county_of_prosecutor', sa.String(length=64), nullable=True),
    sa.Column('judge_name', sa.Text(), nullable=True),
    sa.Column('division_name', sa.Text(), nullable=True),
    sa.Column('petitioner_name', sa.Text(), nullable=True),
    sa.Column('division_number', sa.Text(), nullable=True),
    sa.Column('city_name_here', sa.Text(), nullable=True),
    sa.Column('county_name', sa.Text(), nullable=True),
    sa.Column('arresting_county', sa.Text(), nullable=True),
    sa.Column('prosecuting_county', sa.Text(), nullable=True),
    sa.Column('arresting_municipality', sa.Text(), nullable=True),
    sa.Column('other_agencies_name', sa.Text(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('modified_by', sa.Integer(), nullable=True),
    sa.Column('purged_by', sa.Integer(), nullable=True),
    sa.Column('cms_case_number', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('qualifying__answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_session', sa.String(length=250), nullable=True),
    sa.Column('question_id', sa.String(length=250), nullable=True),
    sa.Column('answer', sa.Text(), nullable=True),
    sa.Column('qualifying_answer', sa.String(length=250), nullable=True),
    sa.Column('question_version_number', sa.Float(asdecimal=True), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('answerer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answerer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_qualifying__answer_timestamp'), 'qualifying__answer', ['timestamp'], unique=False)
    op.create_index(op.f('ix_qualifying__answer_user_session'), 'qualifying__answer', ['user_session'], unique=False)
    op.create_table('conviction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('case_number', sa.String(length=64), nullable=True),
    sa.Column('agency', sa.String(length=64), nullable=True),
    sa.Column('court_name', sa.String(length=64), nullable=True),
    sa.Column('court_city_county', sa.String(length=64), nullable=True),
    sa.Column('judge', sa.String(length=128), nullable=True),
    sa.Column('record_name', sa.String(length=128), nullable=True),
    sa.Column('release_status', sa.String(length=64), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('arrest_date', sa.String(length=64), nullable=True),
    sa.Column('created_by', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('charge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conviction_id', sa.Integer(), nullable=True),
    sa.Column('charge', sa.String(length=128), nullable=True),
    sa.Column('citation', sa.String(length=128), nullable=True),
    sa.Column('sentence', sa.String(length=128), nullable=True),
    sa.Column('conviction_class_type', sa.String(length=64), nullable=True),
    sa.Column('conviction_charge_type', sa.String(length=64), nullable=True),
    sa.Column('eligible', sa.String(length=64), nullable=True),
    sa.Column('please_expunge', sa.String(length=64), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('conviction_description', sa.String(length=256), nullable=True),
    sa.Column('to_print', sa.Text(), nullable=True),
    sa.Column('convicted', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['conviction_id'], ['conviction.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('charge')
    op.drop_table('conviction')
    op.drop_index(op.f('ix_qualifying__answer_user_session'), table_name='qualifying__answer')
    op.drop_index(op.f('ix_qualifying__answer_timestamp'), table_name='qualifying__answer')
    op.drop_table('qualifying__answer')
    op.drop_table('client')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('qualifying__question')
    # ### end Alembic commands ###