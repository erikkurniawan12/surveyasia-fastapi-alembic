from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field
from typing import List
from typing import Optional


class UsernameBase(BaseModel):
    username: Optional[str] = None

class UsernameTimestamp(UsernameBase):
    updated_at: str = Field(default=datetime.utcnow() + timedelta(hours=7), exclude=False)