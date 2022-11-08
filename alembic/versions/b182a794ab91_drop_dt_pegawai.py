"""drop dt_pegawai

Revision ID: b182a794ab91
Revises: 56fbeead43e9
Create Date: 2022-11-08 19:34:19.862811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b182a794ab91'
down_revision = '56fbeead43e9'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_table('dt_pegawai')
