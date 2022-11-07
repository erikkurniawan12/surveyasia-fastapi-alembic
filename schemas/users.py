from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field
from typing import List


class Register(BaseModel):
    username: str = Field(..., example='test')
    email: str = Field(...)
    telp: str = Field(..., example='+6285999123456')
    password: str = Field(..., example='surveyas123')

class responseRegister(Register):
    id: int

class Registeris(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[responseRegister]

class confirmPassword(Register):
    confirm_password: str = Field(..., example='surveyas123')
    created_at: str = Field(default=datetime.utcnow() + timedelta(hours=7), exclude=False)
    updated_at: str = Field(default=datetime.utcnow() + timedelta(hours=7), exclude=False)