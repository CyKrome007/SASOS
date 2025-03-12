from typing import Optional

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import Response
from fastapi.requests import Request

from backend.const.api import AuthEndpoints
from backend.scripts.core.handlers.auth import AuthHandler
from backend.scripts.core.models.users import UserLogin, UserRegister


router = APIRouter(prefix=AuthEndpoints.PREFIX, tags=AuthEndpoints.TAGS)

handler = AuthHandler()

@router.post(AuthEndpoints.LOGIN)
async def login(response: Response, payload: UserLogin):
    result = handler.login(response, payload)
    return result

@router.post(AuthEndpoints.REGISTER)
async def register(response: Response,
                   email: str = Form(...),
                   name: str = Form(...),
                   phone: Optional[str] = Form(None),
                   password: str = Form(...),
                   confirm_password: str = Form(...),
                   avatar: UploadFile = File(...)):
    payload = UserRegister(email=email, name=name, phone=phone, password=password, confirm_password=confirm_password)
    result = handler.register(response, payload, avatar)
    return result

