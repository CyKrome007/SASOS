from pymongo import MongoClient

from backend.const.application_configuration import db_conf
from backend.scripts.core.logger import logger


try:
    client = MongoClient(db_conf.URI)
    db = client[db_conf.NAME]
    user_collection = db[db_conf.USER_COLLECTION]
    logger.info('Successfully connected to MongoDB.')
except Exception as e:
    logger.error('There was some error while connecting to MongoDB:')
    logger.error(e)