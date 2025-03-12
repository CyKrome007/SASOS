from fastapi import Response
import jwt
from passlib.context import CryptContext

from backend.const.application_configuration import auth_conf
from backend.scripts.core.logger import logger

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_ctx.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_ctx.hash(password)

def encode_payload(payload: dict) -> str:
    return jwt.encode(
        payload=payload,
        key=auth_conf.SECRET_KEY,
        algorithm=auth_conf.ALGORITHM
    )

def decode_token(token: str) -> dict:
    return jwt.decode(
        jwt=token,
        key=auth_conf.SECRET_KEY,
        algorithms=[auth_conf.ALGORITHM]
    )

def create_cookie(response: Response, payload: dict) -> None:
    try:
        payload = encode_payload(payload)
        response.set_cookie(
            key=auth_conf.COOKIE_NAME,
            value=payload,
            httponly=auth_conf.HTTP_ONLY
        )
    except Exception as e:
        logger.error(e)
