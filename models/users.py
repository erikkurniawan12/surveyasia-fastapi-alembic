from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    BigInteger, 
    Enum, 
    TIMESTAMP
)
from sqlalchemy.sql.sqltypes import Date
import sqlalchemy as sa

metadata = MetaData()


tbl_users = Table(
    "tbl_users", 
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
    sa.Column('nama_lengkap', sa.String(255), nullable=False),
    sa.Column('username', sa.String(255), nullable=False),
    sa.Column('email', sa.String(255), nullable=False),
    sa.Column('telp', sa.String(255), nullable=False),
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
    sa.Column('email_verified_at', sa.TIMESTAMP, nullable=True),
    sa.Column('biodata_id', sa.BigInteger, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP, nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
)


tbl_biodata = Table(
    'tbl_biodata', 
    metadata, 
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger, nullable=False), 
    sa.Column('nik', sa.BigInteger, nullable=False),
    sa.Column('nama_lengkap', sa.String(255), nullable=False),
    sa.Column('telp', sa.String(255), nullable=False),
    sa.Column('gender', sa.Enum('Laki-laki','Perempuan'), nullable=True),
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