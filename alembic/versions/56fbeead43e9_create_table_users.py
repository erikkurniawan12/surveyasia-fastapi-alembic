"""create table users

Revision ID: 56fbeead43e9
Revises: 794b68f0d2f9
Create Date: 2022-11-07 23:04:04.589909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56fbeead43e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dt_karyawan',
        sa.Column('id_pegawai', sa.Integer, primary_key=True),
        sa.Column('nama_pegawai', sa.String(255), nullable=False),
        sa.Column('alamat_pegawai', sa.String(255)),
        sa.Column('ttl_pegawai', sa.Date()),
        sa.Column('telp_pegawai', sa.String(255)),
        sa.Column('email_pegawai', sa.String(255), unique=True)
    )
    


def downgrade():
    op.drop_table('dt_pegawai')
