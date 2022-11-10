"""create table tbl_questions

Revision ID: 467e16f2bb73
Revises: 797db8b1f750
Create Date: 2022-11-10 08:37:34.517704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '467e16f2bb73'
down_revision = '797db8b1f750'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tbl_questions', 
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('survey_id', sa.BigInteger, nullable=False),
        sa.Column('question', sa.String(255), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True)
    )
    op.create_foreign_key(
        constraint_name='fk_questions_surveys', 
        source_table='tbl_questions', 
        referent_table='tbl_surveys', 
        local_cols=['survey_id'], 
        remote_cols=['id']
    )


def downgrade():
    op.drop_table(
        table_name='tbl_questions'
    )
