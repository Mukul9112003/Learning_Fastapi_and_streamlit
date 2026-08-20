import streamlit as st
import requests 
st.title("Learning request")
st.subheader("Day2")
c1='''
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
app=FastAPI()
class data_request(BaseModel):
    id:int | None=None
    name:str | None=None
    age:int | None=None
    gender:str | None=None
patients=[{"id":1,"name":"Rahul","age":18,"gender":"M"},{"id":2,"name":"harry","age":18,"gender":"M"}]
@app.get("/data")
def get_request():
    return {
        "data":patients
    }
@app.post("/add_patient",status_code=status.HTTP_201_CREATED)
def post_request(data:data_request):
    for patient in patients:
        if data.id in patient["id"]:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Patient already exist"
            )
    patients.append(data.model_dump())
    return{
        "message":data
    }
'''
st.code(c1,language="python")
id=st.number_input("Enter your id")
name=st.text_input("Enter name")
age=st.number_input("Enter your age")
st.text("M for Male or F for Female")
gender=st.text_input("Enter gender")
if st.button("Click to send data"):
    data={
        "id":int(id),"name":name,"age":int(age),"gender":gender
    }
    response=requests.post("http://localhost:8000/add_patient",json=data)
    st.success(response.json())
if st.button("show data base"):
     response=requests.get("http://localhost:8000/data")
     st.success(response.json())