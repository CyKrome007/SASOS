import configparser
import os
import sys
import dotenv

try:
    config = configparser.ConfigParser()
    CONFIG_FILE_PATH = r'backend/config/.conf'
    config.read(CONFIG_FILE_PATH)

    if not os.path.exists(CONFIG_FILE_PATH):
        print('Configuration file not found. Exiting...')
        sys.exit(0)

    DOTENV_FILE_PATH = r'.env'
    dotenv.load_dotenv(DOTENV_FILE_PATH)
except Exception as e:
    print('Something went wrong while configuring the application:')
    print(e.__str__())
    print('Exiting...')
    sys.exit(0)

class ApplicationConfiguration:
    NAME = os.getenv('APP_NAME', config.get('App', 'APP_NAME'))
    DESCRIPTION = os.getenv('APP_DESCRIPTION', config.get('App', 'APP_DESCRIPTION'))
    VERSION = os.getenv('APP_VERSION', config.get('App', 'APP_VERSION'))
    API_VERSION_ROUTE = os.getenv('API_VERSION_ROUTE', config.get('App', 'API_VERSION_ROUTE'))
    STRING = os.getenv('APP_STRING', config.get('App', 'APP_STRING'))
    HOST = os.getenv('APP_HOST', config.get('App', 'APP_HOST'))
    PORT = int(os.getenv('APP_PORT', config.get('App', 'APP_PORT')))
    RELOAD = bool(os.getenv('RELOAD', config.get('App', 'RELOAD')))
    RESPONSE_SUCCESS_FIELD = os.getenv('RESPONSE_SUCCESS_FIELD', config.get('App', 'RESPONSE_SUCCESS_FIELD'))
    RESPONSE_MESSAGE_FIELD = os.getenv('RESPONSE_MESSAGE_FIELD', config.get('App', 'RESPONSE_MESSAGE_FIELD'))
    RESPONSE_DATA_FIELD = os.getenv('RESPONSE_DATA_FIELD', config.get('App', 'RESPONSE_DATA_FIELD'))

class BusinessConfiguration:
    USER_AVATAR_PATH = os.getenv('USER_AVATAR_PATH', config.get('Business', 'USER_AVATAR_PATH'))
    LAND_PATH = os.getenv('LAND_PATH', config.get('Business', 'LAND_PATH'))

class DatabaseConfiguration:
    URI = os.getenv('DB_URI', config.get('Database', 'DB_URI'))
    NAME = os.getenv('DB_NAME', config.get('Database', 'DB_NAME'))
    USER_COLLECTION = os.getenv('USER_COLLECTION', config.get('Database', 'USER_COLLECTION'))
    # DB_PORT = int(os.getenv('DB_PORT', config.get('Database', 'DB_PORT')))
    # DB_PASSWORD = os.getenv('DB_PASSWORD', config.get('Database', 'DB_PASSWORD'))

class AuthConfiguration:
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', config.get('Auth', 'JWT_SECRET_KEY'))
    ALGORITHM = os.getenv('JWT_ALGORITHM', config.get('Auth', 'JWT_ALGORITHM'))
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', config.get('Auth', 'ACCESS_TOKEN_EXPIRE_MINUTES')))
    COOKIE_NAME = os.getenv('COOKIE_NAME', config.get('Auth', 'COOKIE_NAME'))
    HTTP_ONLY = bool(os.getenv('HTTP_ONLY', config.get('Auth', 'HTTP_ONLY')))
    SAME_SITE = os.getenv('SAME_SITE', config.get('Auth', 'SAME_SITE'))
    SCHEMES = os.getenv('PASSLIB_SCHEMES', config.get('Auth', 'PASSLIB_SCHEMES')).split(' ')
    COOKIE_FIELD = os.getenv('COOKIE_FIELD', config.get('Auth', 'COOKIE_FIELD'))

class LoggingConfiguration:
    LOG_FILE_NAME = os.getenv('LOG_FILE_NAME', config.get('Logger', 'LOG_FILE_NAME'))
    LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', config.get('Logger', 'LOG_FILE_PATH'))
    LOG_LEVEL = os.getenv('LOG_LEVEL', config.get('Logger', 'LOG_LEVEL'))
    LOG_FILE_MAX_BYTES = int(os.getenv('LOG_FILE_MAX_BYTES', config.get('Logger', 'LOG_FILE_MAX_BYTES')))
    LOG_FILE_BACKUP_COUNT = int(os.getenv('LOG_FILE_BACKUP_COUNT', config.get('Logger', 'LOG_FILE_BACKUP_COUNT')))

app_conf = ApplicationConfiguration()
business_conf = BusinessConfiguration()
db_conf = DatabaseConfiguration()
auth_conf = AuthConfiguration()
log_conf = LoggingConfiguration()
