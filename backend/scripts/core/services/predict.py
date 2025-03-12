from fastapi import APIRouter
from starlette.requests import Request

from backend.const.api import PredictionEndpoints
from backend.scripts.core.handlers.predict import PredictionHandler
from backend.scripts.core.models.predict import PredictCrop

router = APIRouter(prefix=PredictionEndpoints.PREFIX, tags=PredictionEndpoints.TAGS)

handler = PredictionHandler()

@router.post(PredictionEndpoints.PREDICT)
async def predict_crop(request: Request, payload: PredictCrop):
    result = handler.predict_crop(request, payload)
    return result
