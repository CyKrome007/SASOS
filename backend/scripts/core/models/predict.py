from pydantic import BaseModel


class PredictCrop(BaseModel):
    N: float = 90
    P: float = 42
    K: float = 43
    temperature: float = 20.87
    humidity: float = 92.80
    ph: float = 6.50
    rainfall: float = 202.93
