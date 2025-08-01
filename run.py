# run.py

from fastapi import FastAPI
from app.db import Base, engine
from app.routes import user, student, teacher

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(user.router, prefix="/api/users", tags=["Users"])
app.include_router(teacher.router, prefix="/api/teachers", tags=["Teachers"])
app.include_router(student.router, prefix="/api/students", tags=["Students"])