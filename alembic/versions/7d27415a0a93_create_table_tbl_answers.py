"""create table tbl_answers

Revision ID: 7d27415a0a93
Revises: 467e16f2bb73
Create Date: 2022-11-10 08:48:14.649318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d27415a0a93'
down_revision = '467e16f2bb73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tbl_answers', 
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('user_id', sa.BigInteger, nullable=False),
        sa.Column('question_id', sa.BigInteger, nullable=False),
        sa.Column('answer', sa.Text, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
    )
    op.create_foreign_key(
        constraint_name='fk_answers_users', 
        source_table='tbl_answers', 
        referent_table='tbl_users', 
        local_cols=['user_id'], 
        remote_cols=['id']
    )
    op.create_foreign_key(
        constraint_name='fk_answers_questions', 
        source_table='tbl_answers', 
        referent_table='tbl_questions', 
        local_cols=['question_id'], 
        remote_cols=['id']
    )
    op.create_unique_constraint(
        constraint_name='uq_answers_questions', 
        table_name='tbl_answers', 
        columns=['question_id'],
    )


def downgrade():
    op.drop_table(
        table_name='tbl_answers'
    )
