from pydantic import BaseModel
from enum import Enum

class UserOut(BaseModel): 
    username: str
    role: str

    class Config: 
        from_attributes = True

class Role(str, Enum):
    student = "Student"
    teacher = "Teacher"

class UserCreate(BaseModel): 
    username: str
    password: str
    role: Role = Role.student

class UserLogin(BaseModel): 
    username: str
    password: str