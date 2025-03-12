from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from backend.const.api import AuthEndpoints
from backend.const.application_configuration import auth_conf, app_conf
from backend.scripts.utils.auth import decode_token


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.__EXCLUDED_ROUTES__ = [
            '/',
            '/docs',
            '/redoc',
            '/openapi.json',
            app_conf.API_VERSION_ROUTE + AuthEndpoints.PREFIX + AuthEndpoints.LOGIN,
            app_conf.API_VERSION_ROUTE + AuthEndpoints.PREFIX + AuthEndpoints.REGISTER
        ]


    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        for route in self.__EXCLUDED_ROUTES__:
            if request.url.path == route:
                response = await call_next(request)
                return response
        token = request.cookies.get(auth_conf.COOKIE_NAME)
        if not token:
            return JSONResponse(
                status_code=401,
                content={
                    app_conf.RESPONSE_SUCCESS_FIELD: False,
                    app_conf.RESPONSE_MESSAGE_FIELD: 'You are not logged in'
                }
            )

        user_id = decode_token(token)
        if not user_id:
            return JSONResponse(
                status_code=401,
                content={
                    app_conf.RESPONSE_SUCCESS_FIELD: False,
                    app_conf.RESPONSE_MESSAGE_FIELD: 'You are not logged in'
                }
            )

        request.state.user_id = user_id.get(auth_conf.COOKIE_FIELD)
        request.state.is_authenticated = True

        response = await call_next(request)
        return response