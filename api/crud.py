# crud.py
from sqlalchemy.orm import Session
from models import Detection

def get_all_detections(db: Session):
    return db.query(Detection).all()

def create_detection(db: Session, detection: Detection):
    db.add(detection)
    db.commit()
    db.refresh(detection)
    return detection