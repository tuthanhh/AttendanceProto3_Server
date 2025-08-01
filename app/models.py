import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID  

from app.db import Base
from datetime import datetime

class User(Base): 
    __tablename__ = "user"
    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    role = Column(String, default="Student")

class RollCall(Base):
    __tablename__ = "roll_call"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow)

class Attendance(Base): 
    __tablename__ = "attendance"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    roll_call_id = Column(UUID(as_uuid=True), ForeignKey("roll_call.id"))
    student_username = Column(String, ForeignKey("user.username"))
    timestamp = Column(DateTime, default=datetime.utcnow)