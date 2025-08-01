from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud, auth_utils
from app.db import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)): 
    existing = crud.get_user_by_username(db, user.username)
    if existing: 
        raise HTTPException(status_code=400, detail= "Username already exists")
    return crud.create_user(db, user)

@router.post("/login") 
def login(user: schemas.UserLogin, db: Session = Depends(get_db)): 
    db_user = crud.get_user_by_username(db, user.username)
    if not db_user or not auth_utils.verify_password(user.password, db_user.password): 
        raise HTTPException(status_code=401, detail="Wrong account or password")
    return {"message": "Login successful", "role": db_user.role}