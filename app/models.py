from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class User(Base): 
    __tablename__ = "user"
    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    role = Column(String, default="Student")