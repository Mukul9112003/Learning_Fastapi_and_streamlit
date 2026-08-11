import requests
import streamlit as st

st.title("Day 3 of learning")
code='''
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
'''
response = requests.get("http://127.0.0.1:8000/home")

st.write(response.json())
number=st.number_input("Enter patient id",min_value=1,
    step=1)
if st.button("Get Patient"):

    response = requests.get(
        f"http://127.0.0.1:8000/home/{number}"
    )

    st.write(response.json())
st.code(code,language="python")    