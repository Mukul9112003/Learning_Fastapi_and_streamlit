from Database.sql_dataconnection import engine, get_database
from fastapi import Depends, FastAPI
from Model.base import Base
from repository.User.databases import Sql_Database
from Services.user_service import UserService
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app=FastAPI(title="this is my first backend")
app.get("/")
def get_data():
    return {"message":"first page"}

@app.post("/register")
def register_user(data: dict,
    session: Session = Depends(get_database)):
    db=Sql_Database(session=session)
    user=UserService(db)
    return {
        "message":user.register(data)}