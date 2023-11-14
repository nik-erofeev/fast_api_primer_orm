from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RegisterUser(BaseModel):
    name: str
    fullname: Optional[str] = None


class User(RegisterUser):
    id: int
    created_at: Optional[datetime] = None
