from fastapi import status
from starlette.responses import JSONResponse, Response
from starlette.requests import Request

from backend.const.application_configuration import app_conf, auth_conf
from backend.scripts.core.logger import logger
from backend.scripts.utils import convert_str_to_id, convert_id_to_str, remove_password
from backend.scripts.utils.mongo import user_collection


class UsersHandler:
    def __init__(self):
        pass

    def logout(self, request: Request, response: Response):
        try:
            user_id = request.state.user_id
            if not user_id:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={
                        app_conf.RESPONSE_SUCCESS_FIELD: False,
                        app_conf.RESPONSE_MESSAGE_FIELD: 'You are not logged in'
                    }
                )
            response.delete_cookie(auth_conf.COOKIE_NAME)
            return {
                app_conf.RESPONSE_SUCCESS_FIELD: True,
                app_conf.RESPONSE_MESSAGE_FIELD: 'Logged out successfully'
            }
        except Exception as e:
            logger.error('Something went wrong while logging out:')
            logger.error(e)
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    app_conf.RESPONSE_SUCCESS_FIELD: False,
                    app_conf.RESPONSE_MESSAGE_FIELD: 'Something went wrong'
                }
            )

    def profile(self, request: Request):
        try:
            user_id = request.state.user_id
            if not user_id:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={
                        app_conf.RESPONSE_SUCCESS_FIELD: False,
                        app_conf.RESPONSE_MESSAGE_FIELD: 'You are not logged in'
                    }
                )

            user_id = convert_str_to_id(user_id)
            user = user_collection.find_one({'_id': user_id})
            if not user:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        app_conf.RESPONSE_SUCCESS_FIELD: False,
                        app_conf.RESPONSE_MESSAGE_FIELD: "User Doesn't Exists"
                    }
                )

            user = convert_id_to_str(user)
            user = remove_password(user)

            return {
                app_conf.RESPONSE_SUCCESS_FIELD: True,
                app_conf.RESPONSE_DATA_FIELD: user
            }
        except Exception as e:
            logger.error('Something went wrong while getting the user profile:')
            logger.error(e)
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    app_conf.RESPONSE_SUCCESS_FIELD: False,
                    app_conf.RESPONSE_MESSAGE_FIELD: 'Something went wrong'
                }
            )