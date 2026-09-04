from Model.user_model import create_request,login_request
from sqlalchemy.orm import Session
from database.database_connection import db_session
from database.Model import User
from fastapi import APIRouter,Depends,HTTPException,status
user=APIRouter()
@user.post("/register")
def create_user(data:create_request,db:Session=Depends(db_session)):
    check=db.query(User).filter(User.email==data.email).first()
    if check:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already used ")
    user = User(
            email=data.email,
            password=data.password
    )
    db.add(user)
    db.commit()
    return {
        "message": "User registered successfully"
    }
@user.post("/login")
def login_user(data: login_request,db: Session = Depends(db_session)):
    check = db.query(User).filter(User.email == data.email).first()

    if not check:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if check.password != data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful"
    }