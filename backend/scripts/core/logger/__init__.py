import logging
import sys
from logging.handlers import RotatingFileHandler

from backend.const.application_configuration import log_conf, app_conf

logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        RotatingFileHandler(
            filename=log_conf.LOG_FILE_PATH + log_conf.LOG_FILE_NAME,
            maxBytes=log_conf.LOG_FILE_MAX_BYTES,
            backupCount=log_conf.LOG_FILE_BACKUP_COUNT),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(app_conf.NAME)
