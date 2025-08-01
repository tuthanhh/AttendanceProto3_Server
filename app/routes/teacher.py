from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db import get_db

router = APIRouter()

# Route to create roll call 
@router.post("/roll_call/create")
def create_roll_call(timestamp: str = None, db: Session = Depends(get_db)):
    try:
        roll_call = crud.create_roll_call(db, timestamp)
        return {"message": "Roll call created successfully", "roll_call_id": roll_call.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/roll_call/{roll_call_id}")
def get_roll_call(roll_call_id: str, db: Session = Depends(get_db)):
    roll_call = crud.get_roll_call(db, roll_call_id)
    if not roll_call:
        raise HTTPException(status_code=404, detail="Roll call not found")
    return roll_call

@router.get("/roll_call/{roll_call_id}/attendance")
def get_attendance(roll_call_id: str, db: Session = Depends(get_db)):
    attendance_records = crud.get_attendance_by_roll_call(db, roll_call_id)
    if not attendance_records:
        raise HTTPException(status_code=404, detail="No attendance records found for this roll call")
    return attendance_records
