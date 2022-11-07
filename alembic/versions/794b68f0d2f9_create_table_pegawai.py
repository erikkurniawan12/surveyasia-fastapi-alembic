"""create table pegawai

Revision ID: 794b68f0d2f9
Revises: 
Create Date: 2022-10-26 14:24:25.712679

"""
from alembic import op
import sqlalchemy as sa
from faker import Faker
from models.users import tbl_users

faker = Faker('id_ID')


# revision identifiers, used by Alembic.
revision = '794b68f0d2f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pgw = op.create_table(
        'dt_pegawai',
        sa.Column('id_pegawai', sa.Integer, primary_key=True),
        sa.Column('nama_pegawai', sa.String(255), nullable=False),
        sa.Column('alamat_pegawai', sa.String(255)),
        sa.Column('ttl_pegawai', sa.Date()),
        sa.Column('telp_pegawai', sa.String(255)),
        sa.Column('email_pegawai', sa.String(255), unique=True)
    )


def downgrade():
    op.drop_table('dt_pegawai')
