"""create table tbl biodata

Revision ID: d48be5325592
Revises: cada040b722b
Create Date: 2022-11-10 01:35:10.659564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd48be5325592'
down_revision = 'cada040b722b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tbl_biodata',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('user_id', sa.BigInteger, nullable=False), 
        sa.Column('nik', sa.BigInteger, nullable=False),
        sa.Column('nama_lengkap', sa.String(255), nullable=False),
        sa.Column('telp', sa.String(255), nullable=False),
        sa.Column('gender', sa.Enum('Laki-laki','Perempuan'), nullable=False),
        sa.Column('birth_place', sa.String(50), nullable=False),
        sa.Column('birth_date', sa.Date(), nullable=False),
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
        sa.Column('job', sa.String(255), nullable=False),
        sa.Column('job_location', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
    )
    op.create_foreign_key(
        constraint_name='fk_biodata_users', 
        source_table='tbl_biodata', 
        referent_table='tbl_users', 
        local_cols=['user_id'], 
        remote_cols=['id']
    )
    op.create_unique_constraint(
        constraint_name='uq_biodata_userid', 
        table_name='tbl_biodata', 
        columns=['user_id']
    )


def downgrade():
    op.drop_table(
        table_name='tbl_biodata'
    )
