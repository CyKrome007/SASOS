import uvicorn

from backend.const.application_configuration import app_conf
from backend.scripts.core.logger import logger

if __name__ == "__main__":
    uvicorn.run(app=app_conf.STRING, host=app_conf.HOST, port=app_conf.PORT, reload=app_conf.RELOAD)
    logger.info("Server Closed Successfully.")
