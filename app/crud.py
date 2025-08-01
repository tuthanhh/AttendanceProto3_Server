from sqlalchemy.orm import Session 
from app import models, schemas
from app.auth_utils import *
from datetime import datetime

def create_user(db: Session, user: schemas.UserCreate):
    hashed = hash_password(user.password)
    db_user = models.User(username=user.username, password=hashed, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_roll_call(db: Session, timestamp: datetime = None):
    roll_call = models.RollCall(created_at=timestamp or datetime.utcnow())
    db.add(roll_call)
    db.commit()
    db.refresh(roll_call)
    return roll_call

def create_attendance(db: Session, attendance: schemas.AttendanceCreate):
    existing = db.query(models.Attendance).filter_by(
        roll_call_id=attendance.roll_call_id,
        student_username=attendance.student_username
    ).first()
    
    if existing:
        raise ValueError("Attendance already recorded for this student in this roll call")

    db_attendance = models.Attendance(
        roll_call_id=attendance.roll_call_id,
        student_username=attendance.student_username,
        timestamp=datetime.utcnow()
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def get_roll_call(db: Session, roll_call_id: str):
    return db.query(models.RollCall).filter(models.RollCall.id == roll_call_id).first()

def get_attendance_by_roll_call(db: Session, roll_call_id: str):
    return db.query(models.Attendance).filter(models.Attendance.roll_call_id == roll_call_id).all()