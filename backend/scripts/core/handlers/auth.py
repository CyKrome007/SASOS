from fastapi import Response, status, UploadFile
from fastapi.responses import JSONResponse

from backend.const.application_configuration import auth_conf, app_conf
from backend.scripts.core.logger import logger
from backend.scripts.core.models.users import UserLogin, UserRegister
from backend.scripts.utils import remove_password, convert_id_to_str, validate_email, validate_phone_number, save_avatar
from backend.scripts.utils.auth import verify_password, create_cookie, get_password_hash
from backend.scripts.utils.mongo import user_collection


class AuthHandler:
    def __init__(self):
        pass

    def login(self, response: Response, payload: UserLogin):
        try:

            if not validate_email(payload.email):
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={'message': 'Invalid Email'}
                )

            user = user_collection.find_one({'email': payload.email})

            if not user:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={'message': 'Invalid Email'}
                )

            if not verify_password(payload.password, user.get('password')):
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={'message': 'Incorrect Password'}
                )

            cookie_payload = {auth_conf.COOKIE_FIELD: user.get('_id').__str__()}

            create_cookie(response, cookie_payload)

            user = convert_id_to_str(user)
            user = remove_password(user)

            return {
                app_conf.RESPONSE_SUCCESS_FIELD: True,
                app_conf.RESPONSE_DATA_FIELD: user,
                app_conf.RESPONSE_MESSAGE_FIELD: 'Login Successful'
            }

        except Exception as e:
            logger.error('Something went wrong while registering the user:')
            logger.error(e)
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={'message': 'Something went wrong'}
            )

    def register(self, response: Response, payload: UserRegister, avatar: UploadFile):

        try:
            if payload.email == '' or payload.password == '' or payload.name == '':
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        app_conf.RESPONSE_SUCCESS_FIELD: False,
                        app_conf.RESPONSE_MESSAGE_FIELD: 'Name, Email and Password cannot be empty'
                    }
                )

            if not validate_email(payload.email):
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        app_conf.RESPONSE_SUCCESS_FIELD: False,
                        app_conf.RESPONSE_MESSAGE_FIELD: 'Invalid Email'
                    }
                )

            if payload.phone and not validate_phone_number(payload.phone):
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        app_conf.RESPONSE_SUCCESS_FIELD: False,
                        app_conf.RESPONSE_MESSAGE_FIELD: 'Invalid Phone Number'
                    }
                )

            if payload.password != payload.confirm_password:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        app_conf.RESPONSE_SUCCESS_FIELD: False,
                        app_conf.RESPONSE_MESSAGE_FIELD: 'Passwords do not match'
                    }
                )

            existing_user = user_collection.find_one({'email': payload.email})

            if existing_user:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={'message': 'User with this email already exists'}
                )

            payload.password = get_password_hash(payload.password)
            payload = payload.model_dump()
            if not payload.get('phone'):
                del payload['phone']
            del payload['confirm_password']

            payload.update({'avatar': save_avatar(avatar)})

            new_user_id = user_collection.insert_one(payload)
            new_user = user_collection.find_one({'_id': new_user_id.inserted_id})

            cookie_payload = {auth_conf.COOKIE_FIELD: new_user_id.inserted_id.__str__()}

            new_user = convert_id_to_str(new_user)
            new_user = remove_password(new_user)

            create_cookie(response, cookie_payload)

            return {
                app_conf.RESPONSE_SUCCESS_FIELD: True,
                app_conf.RESPONSE_DATA_FIELD: new_user,
                app_conf.RESPONSE_MESSAGE_FIELD: 'User Registered Successfully'
            }
        except Exception as e:
            logger.error('Something went wrong while registering the user:')
            logger.error(e)
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={'message': 'Something went wrong'}
            )
