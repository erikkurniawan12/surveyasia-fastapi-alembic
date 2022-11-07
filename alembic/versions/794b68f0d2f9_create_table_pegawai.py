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
    op.bulk_insert(
        tbl_users,
        [{'nama_lengkap':faker.name(), 
                 'address':faker.address(),
                 'birth_date':faker.date_of_birth(tzinfo=None, minimum_age=21, maximum_age=28),
                 'telp':faker.phone_number(),
                 'email':faker.email()
                  } for x in range(10)]
    )


def downgrade():
    op.drop_table('tbl_users')
