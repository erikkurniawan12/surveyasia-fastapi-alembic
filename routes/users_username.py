from schemas.users import Register, Registeris, ResponseRegister, ConfirmPassword
from schemas.profile_schema import InformasiPribadiBase, InformasiPribadiTimestamp
from schemas.profile_username_schema import UsernameTimestamp
from models.users import tbl_users, tbl_biodata
from fastapi import APIRouter, Response, status, Request, HTTPException, Depends
from config.database import conn
from fastapi.security import OAuth2PasswordRequestForm
from auth import tokenn, oauth2
from encrypt.hashing import Hash
from auth import tokenn
from auth.oauth2 import get_current_user



username = APIRouter(prefix="/api") 



    

@username.post('/users/profile/username', description="Update username")
async def update_username(req : UsernameTimestamp, response: Response, current_user: ConfirmPassword = Depends(get_current_user)):
    query_1 = tbl_users.update().values(
        username = req.username
    )    
    conn.execute(query_1)
    query_2 = tbl_users.select().filter(
        tbl_users.c.username == req.username
    )
    data = conn.execute(query_2).fetchone()
    response = {
            "code": status.HTTP_201_CREATED, 
            "status": "CREATED", 
            "message": "berhasil mengubah username.", 
            "data": {
                "username": data["username"]
            }
        }
    return response