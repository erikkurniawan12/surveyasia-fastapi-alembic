"""create table tbl_users

Revision ID: cada040b722b
Revises: 
Create Date: 2022-11-08 23:33:07.268219

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import func, TIMESTAMP


# revision identifiers, used by Alembic.
revision = 'cada040b722b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tbl_users',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('nama_lengkap', sa.String(255), nullable=False),
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('telp', sa.String(255), nullable=True),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('remember_token', sa.String(255), nullable=True),
        sa.Column('avatar', sa.String(255), nullable=True), 
        sa.Column('nik', sa.BigInteger, nullable=False),
        sa.Column('birth_place', sa.String(50), nullable=False),
        sa.Column('birth_date', sa.Date(), nullable=False),
        sa.Column('gender', sa.Enum('Laki-laki','Perempuan'), nullable=False),
        sa.Column('job', sa.String(255), nullable=False),
        sa.Column('job_location', sa.String(255), nullable=False),
        sa.Column('ktp_province', sa.String(50), nullable=False),
        sa.Column('ktp_city', sa.String(50), nullable=False),
        sa.Column('ktp_district', sa.String(50), nullable=False),
        sa.Column('ktp_postal_code', sa.BigInteger, nullable=False),
        sa.Column('ktp_address', sa.String(255), nullable=True),
        sa.Column('province', sa.String(50), nullable=False),
        sa.Column('city', sa.String(50), nullable=False),
        sa.Column('district', sa.String(50), nullable=False),
        sa.Column('postal_code', sa.BigInteger, nullable=False),
        sa.Column('address', sa.String(255), nullable=False),
        sa.Column('provider_name', sa.String(255), nullable=True),
        sa.Column('telp_verified_at', sa.TIMESTAMP, nullable=True),
        sa.Column('biodata_id', sa.BigInteger, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, server_default=func.now(), nullable=True),
    )


def downgrade():
    op.drop_table('tbl_users')
