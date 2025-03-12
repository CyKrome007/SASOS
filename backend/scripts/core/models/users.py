from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str

class UserLogin(User):
    pass

class UserRegister(User):
    name: str
    phone: str | Optional[None] = None
    confirm_password: str
