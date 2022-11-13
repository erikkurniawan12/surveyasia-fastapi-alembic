from schemas.users import Register, Registeris, ResponseRegister, ConfirmPassword
from schemas.profile_schema import InformasiPribadiBase, InformasiPribadiTimestamp
from models.users import tbl_users, tbl_biodata
from fastapi import APIRouter, Response, status, Request, HTTPException, Depends
from config.database import conn
from fastapi.security import OAuth2PasswordRequestForm
from auth import tokenn, oauth2
from encrypt.hashing import Hash
from auth import tokenn
from auth.oauth2 import get_current_user



profile = APIRouter(prefix="/api") 



    

@profile.post('/users/profile', description="Update informasi pribadi")
async def update_informasi_pribadi(req : InformasiPribadiTimestamp, response: Response, current_user: ConfirmPassword = Depends(get_current_user)):
    query_1 = tbl_users.update().values(
        nik = req.nik,
        nama_lengkap = req.nama_lengkap,
        email = req.email,
        gender = req.gender,
        birth_place = req.birth_place,
        birth_date = req.birth_date,
        job = req.job,
        job_location = req.job_location,
        province = req.province,
        city = req.city,
        district = req.district,
        postal_code = req.postal_code,
        address = req.address, 
        updated_at = req.updated_at
    )    
    conn.execute(query_1)
    query_2 = tbl_biodata.update().values(
        nik = req.nik,
        nama_lengkap = req.nama_lengkap,
        gender = req.gender,
        birth_place = req.birth_place,
        birth_date = req.birth_date,
        job = req.job,
        job_location = req.job_location,
        province = req.province,
        city = req.city,
        district = req.district,
        postal_code = req.postal_code,
        address = req.address, 
        updated_at = req.updated_at
    )    
    conn.execute(query_2)
    query_3 = tbl_users.select().filter(
        tbl_users.c.email == req.email
    )
    data = conn.execute(query_3).fetchone()
    response = {
            "code": status.HTTP_201_CREATED, 
            "status": "CREATED", 
            "message": "berhasil melangkapi informasi pribadi.", 
            "data": {
                "nik": data["nik"], 
                "nama_lengkap": data["nama_lengkap"],
                "email": data["email"],
                "gender": data["gender"],
                "birth_place": data["birth_place"],
                "birth_date": data["birth_date"],
                "job": data["job"],
                "job_location": data["job_location"],
                "province": data["province"],
                "city": data["city"],
                "district": data["district"],
                "postal_code": data["postal_code"],
                "address": data["address"]
            }
        }
    return response