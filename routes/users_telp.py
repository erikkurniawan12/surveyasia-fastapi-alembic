from schemas.users import Register, Registeris, ResponseRegister, ConfirmPassword
from schemas.profile_schema import InformasiPribadiBase, InformasiPribadiTimestamp
from schemas.profile_username_schema import UsernameTimestamp
from schemas.profile_telp_schema import TelpTimestamp
from models.users import tbl_users, tbl_biodata
from fastapi import APIRouter, Response, status, Request, HTTPException, Depends
from config.database import conn
from fastapi.security import OAuth2PasswordRequestForm
from auth import tokenn, oauth2
from encrypt.hashing import Hash
from auth import tokenn
from auth.oauth2 import get_current_user



telp = APIRouter(prefix="/api") 



    

@telp.post('/users/profile/telp', description="Update nomor ponsel")
async def update_username(req : TelpTimestamp, response: Response, current_user: ConfirmPassword = Depends(get_current_user)):
    query_1 = tbl_users.update().values(
        telp = req.telp, 
        updated_at = req.updated_at
    )    
    conn.execute(query_1)
    query_2 = tbl_biodata.update().values(
        telp = req.telp, 
        updated_at = req.updated_at
    )    
    conn.execute(query_2)
    query_3 = tbl_users.select().filter(
        tbl_users.c.telp == req.telp
    )
    data = conn.execute(query_3).fetchone()
    response = {
            "code": status.HTTP_201_CREATED, 
            "status": "CREATED", 
            "message": "berhasil mengubah nomor ponsel.", 
            "data": {
                "username": data["telp"]
            }
        }
    return response