# schemas.py
from pydantic import BaseModel

class DetectionSchema(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True