import uuid
from pydantic import BaseModel
from enum import Enum
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
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True

class RollCallCreate(BaseModel):
    pass

class AttendanceOut(BaseModel):
    id: uuid.UUID
    roll_call_id: uuid.UUID
    student_username: str
    timestamp: datetime

    class Config:
        from_attributes = True

class AttendanceCreate(BaseModel):
    roll_call_id: uuid.UUID
    student_username: str
