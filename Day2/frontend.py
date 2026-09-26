import streamlit as st

st.header("Second App")
st.markdown(
'''
### this 
## this
#this 
-this
 1. this
 2. this
'''
)
st.write("### this is code")
code='''
from fastapi import FastAPI,status,HTTPException,Request
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
app=FastAPI()
class addres(BaseModel):
    city:str
    pincode:int=Field(...,description="This is pin code",max_digits=6)
class user(BaseModel):
    name:str | None
    age:int=0
    address:addres
l=[]
class MyException(Exception):
    def __init__(self,e):
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
'''
st.code(code,language="python")