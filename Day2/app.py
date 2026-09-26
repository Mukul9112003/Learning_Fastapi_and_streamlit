from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app=FastAPI()
class addres(BaseModel):
    city:str
    pincode:int=Field(...,ge=10,description="6-digit pincode")
class user(BaseModel):
    name:str | None
    age:int=0
    address:addres
l=[]
class MyException(Exception):
    def __init__(self,e):
        super().__init__(str(e))
        self.error=e
@app.exception_handler(MyException)
def handler(request:Request,exc:MyException):
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "message": str(exc.error)
        }
    )
@app.post("/add/{page}",status_code=status.HTTP_201_CREATED)
def addition_function(page:int,data:user):
    try:
        result=data.address.pincode/data.age
        l.append(data)
        return {"result": result}
    except Exception as e:
        raise MyException(e)