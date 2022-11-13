from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field
from typing import List
from typing import Optional


class InformasiPribadiBase(BaseModel):
    nik: Optional[str] = None
    nama_lengkap: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    birth_place: Optional[str] = None
    birth_date: Optional[date] = None
    job: Optional[str] = None
    job_location: Optional[str] = None
    province: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    postal_code: Optional[str] = None
    address: Optional[str] = None

class InformasiPribadiTimestamp(InformasiPribadiBase):
    updated_at: str = Field(default=datetime.utcnow() + timedelta(hours=7), exclude=False)