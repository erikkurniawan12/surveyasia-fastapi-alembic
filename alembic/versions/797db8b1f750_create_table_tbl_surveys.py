"""create table tbl_surveys

Revision ID: 797db8b1f750
Revises: 0b72ba44e274
Create Date: 2022-11-10 08:24:57.052380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '797db8b1f750'
down_revision = '0b72ba44e274'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tbl_surveys', 
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('surveycategory_id', sa.BigInteger, nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('author', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('survey_point', sa.BigInteger, nullable=False),
        sa.Column('status', sa.String(255), nullable=True),
        sa.Column('expired_at', sa.TIMESTAMP, nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
    )
    op.create_foreign_key(
        constraint_name='fk_surveys_surveycategories', 
        source_table='tbl_surveys', 
        referent_table='tbl_surveyCategories', 
        local_cols=['surveycategory_id'], 
        remote_cols=['id']
    )

def downgrade():
    pass
