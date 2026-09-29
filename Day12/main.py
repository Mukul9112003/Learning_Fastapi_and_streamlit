from fastapi import FastAPI,Depends
from utils.dependency import get_user_service
from pydantic import BaseModel


class RegisterRequest(BaseModel):
    name: str
    email: str
app=FastAPI(title="Day 12")
@app.get("/")
def get_home():
    return {"message":"This is Day 12"}



@app.post("/register")
def register(data:RegisterRequest,user_service=Depends(get_user_service)):

    return user_service.register(data)
