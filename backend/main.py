from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.const.application_configuration import app_conf, business_conf
from backend.scripts.core.logger import logger
from backend.scripts.core.middleware.auth_middleware import AuthMiddleware
from backend.scripts.core.services.auth import router as auth_router
from backend.scripts.core.services.users import router as user_router
from backend.scripts.core.services.predict import router as predict_router

app = FastAPI(
    title=app_conf.NAME,
    description=app_conf.DESCRIPTION,
    version=app_conf.VERSION
)

app.mount("/images/user_avatar", StaticFiles(directory=business_conf.USER_AVATAR_PATH), name="user_avatar")
app.mount("/images/land_images", StaticFiles(directory=business_conf.LAND_PATH), name="land_images")

app.add_middleware(AuthMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:5173', 'http://127.0.0.1:5173'],
    allow_credentials = True,
    allow_methods = ['GET', 'POST'],
    allow_headers = ['*']
)

base_router = APIRouter(prefix=app_conf.API_VERSION_ROUTE)
base_router.include_router(auth_router)
base_router.include_router(user_router)
base_router.include_router(predict_router)

app.include_router(base_router)

@app.get("/", response_class=HTMLResponse)
async def root():
    return f"""
<html lang="en">
    <head>
        <title>SASOS</title>
    </head>
    <body>
        <h1>SASOS</h1>
        <p>This is the SASOS API</p>
        <p>Go to <a href="/docs">/docs</a> for API documentation</p>
        <p>Go to <a href="/redoc">/redoc</a> for API documentation</p>
    </body>
</html>
"""

logger.info("Server Started Successfully.")
