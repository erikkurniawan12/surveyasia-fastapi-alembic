"""create table tbl_surveyCategories

Revision ID: 0b72ba44e274
Revises: d48be5325592
Create Date: 2022-11-10 08:16:12.984405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b72ba44e274'
down_revision = 'd48be5325592'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tbl_surveyCategories', 
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('category', sa.Enum('Customers', 'Education', 'Helathcare', 'Employee', 'Market Research'), nullable=False), 
        sa.Column('description', sa.Text, nullable=False), 
        sa.Column('created_at', sa.TIMESTAMP, nullable=True), 
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
    )


def downgrade():
    op.drop_table(
        table_name='tbl_surveyCategories'
    )
