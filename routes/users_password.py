from schemas.users import Register, Registeris, ResponseRegister, ConfirmPassword
from schemas.profile_schema import InformasiPribadiBase, InformasiPribadiTimestamp
from schemas.profile_username_schema import UsernameTimestamp
from schemas.profile_password_schema import PasswordTimestamp
from models.users import tbl_users, tbl_biodata
from fastapi import APIRouter, Response, status, Request, HTTPException, Depends
from config.database import conn
from fastapi.security import OAuth2PasswordRequestForm
from auth import tokenn, oauth2
from encrypt.hashing import Hash
from auth import tokenn
from auth.oauth2 import get_current_user
from encrypt.hashing import Hash



password = APIRouter(prefix="/api") 

    

@password.post('/users/profile/password', description="Update password")
async def update_password(req : PasswordTimestamp, response: Response, current_user: ConfirmPassword = Depends(get_current_user)): 
    query_1 = tbl_users.update().values(
        password = Hash.bcrypt(req.new_password), 
        updated_at = req.updated_at
    )
    if req.new_password != req.confirm_password:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "code": response.status_code, 
            "status": "BAD_REQUEST",
            "message": "Kata sandi tidak cocok", 
            "data": []
        }
    conn.execute(query_1)
    response = {
            "code": status.HTTP_201_CREATED, 
            "status": "CREATED", 
            "message": "berhasil mengubah password.", 
            "data": []
        }
    return response