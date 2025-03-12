from fastapi import APIRouter, Request, Response

from backend.const.api import UserEndpoints
from backend.scripts.core.handlers.users import UsersHandler

router = APIRouter(prefix=UserEndpoints.PREFIX, tags=UserEndpoints.TAGS)

handler = UsersHandler()

@router.get(UserEndpoints.LOGOUT)
async def logout(request: Request, response: Response):
    result = handler.logout(request, response)
    return result

@router.get(UserEndpoints.PROFILE)
async def profile(request: Request):
    result = handler.profile(request)
    return result
