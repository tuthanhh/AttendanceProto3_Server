# run.py

from fastapi import FastAPI
from app.db import Base, engine
from app.routes import user

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/api/users", tags=["Users"])

