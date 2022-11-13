from schemas.users import ConfirmPassword
from models.users import tbl_users, tbl_biodata
from fastapi import APIRouter, Response, status
from config.database import conn
import re
from encrypt.hashing import Hash


register = APIRouter(prefix="/api") 



@register.post('/users/register', description="Registrasi user")
async def register_users(reg : ConfirmPassword, response: Response):
    cek_email = tbl_users.select().filter(tbl_users.c.email == reg.email)
    cek_email = conn.execute(cek_email).fetchone()
    cek_telp = tbl_users.select().filter(tbl_users.c.telp == reg.telp)
    cek_telp = conn.execute(cek_telp).fetchone()
    if cek_email is not None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        json_response =  {
            "code": response.status_code, 
            "status": "BAD_REQUEST",
            "message": "Email telah digunakan", 
            "data": []
        }
        return json_response
    if cek_telp is not None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        json_response = {
            "code": response.status_code, 
            "status": "BAD_REQUEST",
            "message": "Nomor ponsel telah digunakan", 
            "data": []
        }
        return json_response
    if len(reg.username) < 8:
        return {
            "code": status.HTTP_400_BAD_REQUEST, 
            "status": "BAD_REQUEST",
            "message": "Username minimal 8 karakter", 
            "data": []
        }
    if not re.match(r'[^@]+@[^@]+\.[^@]+', reg.email):
        return {
            "code": status.HTTP_400_BAD_REQUEST, 
            "status": "BAD_REQUEST",
            "message": "Email tidak valid", 
            "data": []
        }
    if len(reg.telp) < 8 or len(reg.telp) > 13:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "code": response.status_code, 
            "status": "BAD_REQUEST",
            "message": "Nomor ponsel harus 8 sampai 13 digit", 
            "data": []
        }
    if reg.password != reg.confirm_password:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "code": response.status_code, 
            "status": "BAD_REQUEST",
            "message": "Kata sandi tidak cocok", 
            "data": []
        }
    else:
        query = tbl_users.insert().values(
            username = reg.username,
            email = reg.email,
            telp = reg.telp,
            password = Hash.bcrypt(reg.password),
            is_active = 1,
            created_at = reg.created_at, 
            updated_at = reg.updated_at
        )
        conn.execute(query)
        # insert foreignkey user_id to tbl_biodata
        query_select = tbl_users.select().where(tbl_users.c.email == reg.email)
        data = conn.execute(query_select).fetchone()
        query_2 = tbl_biodata.insert().values(
            user_id = data['id'], 
            telp = data['telp'],
            created_at = data['created_at'], 
            updated_at = data['updated_at']
        )
        conn.execute(query_2)

        # insert foreignkey biodata_id to tbl_users
        query_select_3 = tbl_biodata.select().where(tbl_biodata.c.telp == reg.telp)
        data_3 = conn.execute(query_select_3).fetchone()
        query_3 = tbl_users.update().values(
            biodata_id = data_3['id']
        ).where(tbl_users.c.email == reg.email)
        conn.execute(query_3)
        response = {
            "code": status.HTTP_201_CREATED, 
            "status": "CREATED", 
            "message": "Telah Terdaftar!", 
            "data": [
                {
                    "username": data["username"], 
                    "email": data["email"], 
                    "telp": data["telp"]
                }
            ]
        }
        return response




 




