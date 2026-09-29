from fastapi import Depends, FastAPI
from pydantic import BaseModel
from utils.dependency import get_user_service


class RegisterRequest(BaseModel):
    name: str
    email: str
app=FastAPI(title="Day 12")
@app.get("/")
def get_home():
    return {"message":"This is Day 12"}



@app.post("/register")
def register(data:RegisterRequest,user_service=Depends(get_user_service) ,# noqa: B008
             ):

    return user_service.register(data)
