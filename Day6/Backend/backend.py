from customException.exc import MyException
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from routes.patientRoute import patient

app=FastAPI(title="My Backenend")
@app.exception_handler(MyException)
def excpetion_handler(req:Request,exec:MyException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error":str(exec.e),
            "message":"Check request please"
        }
    )
@app.middleware("http")
async def log_middleware(request:Request,call_next):
    response=await call_next(request)
    print("Middleware work successfully")
    return response
app.include_router(patient)