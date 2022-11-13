from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field
from typing import List
from typing import Optional


class PasswordBase(BaseModel):
    password: Optional[str] = None
    new_password: str = Field(...)
    confirm_password: str = Field(...)

class PasswordTimestamp(PasswordBase):
    updated_at: str = Field(default=datetime.utcnow() + timedelta(hours=7), exclude=False)