from schemas.users import Register, Registeris, ResponseRegister, ConfirmPassword
from models.users import tbl_users, tbl_biodata
from fastapi import APIRouter, Response, status, Request, HTTPException, Depends
from config.database import conn
from fastapi.security import OAuth2PasswordRequestForm
import re
from auth import tokenn, oauth2
from encrypt.hashing import Hash
import json


login = APIRouter(prefix="/api") 


@login.post('/users/login', description="Login user")
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
    query = tbl_users.update().values(
            remember_token = access_token
        ).where(tbl_users.c.email == req.username)
    conn.execute(query).fetchone
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