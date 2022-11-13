from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field
from typing import List
from typing import Optional

class Register(BaseModel):
    username: str = Field(..., example='test')
    email: str = Field(...)
    telp: str = Field(..., example='+6285999123456')
    password: str = Field(..., example='surveyas123')
    is_active: int = Field(default=1, exclude=False)

class ResponseRegister(Register):
    id: int

class Registeris(BaseModel):
    limit: int = Field(default=5)
    offset: int = Field(default=0)
    data: List[ResponseRegister]

class ConfirmPassword(Register):
    confirm_password: str = Field(..., example='surveyas123')
    created_at: str = Field(default=datetime.utcnow() + timedelta(hours=7), exclude=False)
    updated_at: str = Field(default=datetime.utcnow() + timedelta(hours=7), exclude=False)