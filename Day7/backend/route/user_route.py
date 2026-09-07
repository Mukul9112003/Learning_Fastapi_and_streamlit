from fastapi import APIRouter,Depends
users=APIRouter()
from pydantic import BaseModel
class register_user(BaseModel):
    username:str
    password:str
from database.database_connection import db_session
from database.table import user
from sqlalchemy.orm import Session
def register_request(data:register_user,db:Session):
    existing_user=(db.query(user).filter(user.username==data.username).first())
    if existing_user:
        return "username already exists"
    new_user=user(username=data.username,password=hash_password(data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def reset_passwords(new_password):
    pass
def change_complete_user(new_data):
    pass
def delete_request():
    pass
@users.post("/register")
def register(data:register_user,db:Session=Depends(db_session)):
    return {"message":register_request(data,db)}
def reset_password(new_password:str):
    return {"message":reset_passwords(new_password)}
def change_user_and_password(new_data:register_user):
    return {"message":change_complete_user(new_data)}
def delete_user():
    return {"message":delete_request()}