from fastapi import FastAPI,status,HTTPException,Request
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
app=FastAPI()
class number(BaseModel):
    num1:int
    num2:int=Field(default=0)
class user_request(BaseModel):
    name:str=Field(... ,max_length=10)
    add:int=0
    address:str | None=Field(default="almora")
    numbers:number
class user_response(BaseModel):
    name:str
    result:int
l = [
    {"name": "Mukul", "result": 12, "age": 22},
    {"name": "Rahul", "result": 20, "city": "Delhi"}
]
class MyException(Exception):
    def __init__(self,e):
        super().__init__(e)
        self.error=e
@app.exception_handler(MyException)
def MyExceptionHandler(resquest:Request,exc:MyException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error":str(exc.error),
            "message":"Check request please"
        }
    )
class user_response2(BaseModel):
    message:str
@app.get("/user",response_model=list[user_response],status_code=status.HTTP_200_OK)
def send_data():
    return l
@app.post("/user/{page_no}",response_model=user_response2,status_code=status.HTTP_200_OK)
def receive_data(page_no:int,data:user_request):
    try:
        result=data.numbers.num1/data.numbers.num2
        user_data = data.model_dump()   # Convert to dict
        user_data["result"] = result    # Add new field

        l.append(user_data)
    except Exception as e:
        raise MyException(e)
    return {
        "message":"data inserted"
    }