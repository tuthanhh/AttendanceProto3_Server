from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db import get_db

router = APIRouter()

@router.post("/attendance/create")
def create_student_attendance(attendance: schemas.AttendanceCreate, db = Depends(get_db)):
    try: 
        crud.create_attendance(db, attendance)
        return {"message": "Attendance recorded successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))