from pydantic import BaseModel
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID  
from datetime import datetime

class Role(str, Enum):
    student = "Student"
    teacher = "Teacher"

class UserOut(BaseModel): 
    username: str
    role: str

    class Config: 
        from_attributes = True

class UserCreate(BaseModel): 
    username: str
    password: str
    role: Role = Role.student

class UserLogin(BaseModel): 
    username: str
    password: str


class RollCallOut(BaseModel):
    id: UUID
    created_at: datetime


class RollCallCreate(BaseModel):
    pass

class AttendanceOut(BaseModel):
    id: UUID
    roll_call_id: UUID
    student_username: str
    timestamp: datetime

    class Config:
        from_attributes = True

class AttendanceCreate(BaseModel):
    roll_call_id: UUID
    student_username: str