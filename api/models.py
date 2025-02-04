from sqlalchemy import Column, Integer, String, Float
from database import Base

class Detection(Base):
    __tablename__ = "detections"
    image = Column(String, index=True, primary_key=True)
    class_name = Column(String, index=True)
    confidence = Column(Float)
    x_min = Column(Float)
    y_min = Column(Float)
    x_max = Column(Float)
    y_max = Column(Float)
