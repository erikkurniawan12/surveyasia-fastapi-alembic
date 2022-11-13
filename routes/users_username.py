from schemas.users import ConfirmPassword
from schemas.profile_username_schema import UsernameTimestamp
from models.users import tbl_users
from fastapi import APIRouter, Response, status, Depends
from config.database import conn
from auth.oauth2 import get_current_user



username = APIRouter(prefix="/api") 


    

@username.post('/users/profile/username', description="Update username")
async def update_username(req : UsernameTimestamp, response: Response, current_user: ConfirmPassword = Depends(get_current_user)):
    query_1 = tbl_users.update().values(
        username = req.username, 
        updated_at = req.updated_at
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