from backend.const.application_configuration import app_conf
from backend.scripts.core.models.predict import PredictCrop
from backend.scripts.utils.predictor import predict_crop


class PredictionHandler:
    def __init__(self):
        pass

    def predict_crop(self, request, payload: PredictCrop):
        result = predict_crop(**payload.model_dump())
        return {
            app_conf.RESPONSE_SUCCESS_FIELD: True,
            app_conf.RESPONSE_MESSAGE_FIELD: f'Recommended crop for the given conditions: {result}'
        }