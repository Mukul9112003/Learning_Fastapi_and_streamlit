from fastapi import FastAPI,Request,HTTPException,status
from fastapi.responses import JSONResponse
from exception.custom_exception import MyException
from route.patient_route import patient
app=FastAPI()
@app.exception_handler(MyException)
def Exception_handler(req:Request,exc:MyException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "description":exc.error
        }
    )
@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("Request Received")
    response=await call_next(request)
    return response
app.include_router(patient)