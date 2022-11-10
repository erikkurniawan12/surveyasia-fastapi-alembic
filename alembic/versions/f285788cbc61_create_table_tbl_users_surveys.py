"""create table tbl_users_surveys

Revision ID: f285788cbc61
Revises: 7d27415a0a93
Create Date: 2022-11-10 09:33:09.566458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f285788cbc61'
down_revision = '7d27415a0a93'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tbl_users_surveys',  
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('user_id', sa.BigInteger, nullable=False),
        sa.Column('survey_id', sa.BigInteger, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True)
    )
    op.create_foreign_key(
        constraint_name='fk_userssurveys_users', 
        source_table='tbl_users_surveys', 
        referent_table='tbl_users', 
        local_cols=['user_id'], 
        remote_cols=['id']
    )
    op.create_foreign_key(
        constraint_name='fk_userssurveys_surveys', 
        source_table='tbl_users_surveys', 
        referent_table='tbl_surveys', 
        local_cols=['survey_id'], 
        remote_cols=['id']
    )


def downgrade():
    op.drop_table(
        table_name='tbl_users_surveys'
    )
