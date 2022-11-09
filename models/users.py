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

metadata = MetaData()


tbl_users = Table(
    "tbl_users", metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("nama_lengkap", String(255), nullable=False),
    Column("username", String(255)),
    Column("email", String(255)),
    Column("telp", String(255)),
    Column("password", String(255)),
    Column("remember_token", String(255)),
    Column("avatar", String(255)),
    Column("nik", BigInteger),
    Column("birth_place", String(255)),
    Column("birth_date", Date),
    Column("gender", Enum('L', 'P')),
    Column("password", String(255)),
    Column("job", String(255)),
    Column("job_location", String(255)),
    Column("ktp_province", String(255)),
    Column("ktp_city", String(255)),
    Column("ktp_district", String(255)),
    Column("ktp_postal_code", String(255)),
    Column("ktp_address", String(255)),
    Column("province", String(255)),
    Column("city", String(255)),
    Column("district", String(255)),
    Column("postal_code", String(255)),
    Column("address", String(255)),
    Column("provider_name", String(255)),
    Column("telp_verified_at", String(255)),
    Column("created_at", TIMESTAMP),
    Column("updated_at", TIMESTAMP)
)