from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field
from typing import List
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None