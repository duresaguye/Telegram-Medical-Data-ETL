from pydantic import BaseModel

class DetectionSchema(BaseModel):
    image: str
    class_name: str
    confidence: float
    x_min: float
    y_min: float
    x_max: float
    y_max: float

    class Config:
        orm_mode = True