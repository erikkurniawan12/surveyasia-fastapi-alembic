from schemas.users import Register, Registeris, responseRegister, confirmPassword
from models.users import tbl_users
from fastapi import APIRouter, Response, status, Request, HTTPException, Depends
from config.database import conn
from fastapi.security import OAuth2PasswordRequestForm
import re
from auth import tokenn, oauth2
from encrypt.hashing import Hash
import uvicorn

users = APIRouter(prefix="/api") 


@users.get('/users/all', response_model=Registeris, description="Menampilkan semua data")
async def find_all_users(limit: int = 10, offset: int = 0, current_user: confirmPassword = Depends(oauth2.get_current_user)):
    query = tbl_users.select().offset(offset).limit(limit)
    data = conn.execute(query).fetchall()
    response = {
        "code": status.HTTP_200_OK, 
        "status": "OK", 
        "data": data, 
        "pagination": {
            "limit": limit, 
            "offset": offset 
        }
    }
    return response


@users.post('/users/register', description="Registrasi user")
async def register_users(reg : confirmPassword, response: Response):
    cek_email = tbl_users.select().filter(tbl_users.c.email == reg.email)
    cek_email = conn.execute(cek_email).fetchone()
    if cek_email is not None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        json_response =  {
            "code": response.status_code, 
            "status": "BAD_REQUEST",
            "message": "Email telah digunakan", 
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
            created_at = reg.created_at, 
            updated_at = reg.updated_at
        )
        conn.execute(query)
        query_select = tbl_users.select().where(tbl_users.c.email == reg.email)
        data = conn.execute(query_select).fetchone()
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


@users.post('/users/login', description="Login user")
async def login_users(req : OAuth2PasswordRequestForm = Depends()):
    cek_email = tbl_users.select().filter(tbl_users.c.email == req.username)
    cek_email = conn.execute(cek_email).fetchone()
    if not re.match(r'[^@]+@[^@]+\.[^@]+', req.username):
        return {
            "code": status.HTTP_400_BAD_REQUEST, 
            "status": "BAD_REQUEST",
            "message": "Email tidak valid", 
            "data": []
        }
    if not cek_email:
        return {
            "code": status.HTTP_404_NOT_FOUND, 
            "status": "NOT_FOUND", 
            "message": "Tidak Terdaftar!", 
            "data": []
        }
    if not Hash.verify(cek_email.password, req.password):
        return {
            "code": status.HTTP_404_NOT_FOUND, 
            "status": "NOT_FOUND", 
            "message": "Kata sandi tidak cocok", 
            "data": []
        }
    access_token = tokenn.create_access_token(data={"sub": req.username})
    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "info": {
                "code": status.HTTP_200_OK, 
                "status": "OK", 
                "message": "Login berhasil!", 
                "data": {
                    "email": req.username, 
                }
        }     
    } 




