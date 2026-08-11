from fastapi import FastAPI,Request,status
from fastapi.responses import JSONResponse
from Day3.route import mukul
from Day3.custom_exception import MyException
app=FastAPI(title="This is my learning process")
@app.exception_handler(MyException)
def exception_handler(res:Request,exec:MyException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error":str(exec.error),
            "message":"Check request please"
        }
    )
app.include_router(mukul)