# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, database
from database import engine, get_db
from schemas import DetectionSchema

# Initialize FastAPI
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# API to get all detection results
@app.get("/detections", response_model=list[DetectionSchema])
def get_detections(db: Session = Depends(get_db)):
    return crud.get_all_detections(db)

# API to create a new detection
@app.post("/detections", response_model=DetectionSchema)
def create_detection(detection: DetectionSchema, db: Session = Depends(get_db)):
    db_detection = models.Detection(**detection.dict())
    return crud.create_detection(db=db, detection=db_detection)

# Run the server: uvicorn main:app --reload