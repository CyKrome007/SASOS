import uuid

from bson import ObjectId
import re

from backend.const.application_configuration import business_conf


def convert_id_to_str(user: dict) -> dict:
    user['_id'] = user['_id'].__str__()
    return user

def convert_str_to_id(id: str) -> ObjectId:
    result = ObjectId(id)
    return result

def remove_id(user: dict) -> dict:
    user.pop('_id')
    return user

def remove_password(user: dict) -> dict:
    user.pop('password')
    return user

def remove_id_and_password(user: dict) -> dict:
    user = remove_id(user)
    user = remove_password(user)
    return user

# Validating Email Through Regex
email_regex = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"

def validate_email(email):
    return re.match(email_regex, email) is not None

# Validating Phone Through Regex
phone_regex = r"^\+?\d{1,3}[-.\s]?(\(?\d{1,4}\)?[-.\s]?)?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}$"

def validate_phone_number(phone_number):
    return re.match(phone_regex, phone_number) is not None

# Saving User Avatar
def save_avatar(avatar):
    idx = avatar.filename.rfind('.')
    filename = uuid.uuid4().hex
    extension = avatar.filename[idx:]
    with open(f'{business_conf.USER_AVATAR_PATH + filename + extension}', 'wb') as f:
        f.write(avatar.file.read())

    return {
        'filename': filename,
        'extension': extension,
        'url': f'http://localhost:8000/images/user_avatar/{filename + extension}'
    }
