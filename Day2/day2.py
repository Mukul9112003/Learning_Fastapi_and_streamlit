from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
app=FastAPI()
class data_request(BaseModel):
    id:int | None=None
    name:str | None=None
    age:int | None=None
    gender:str | None=None
patients=[{"id":1,"name":"Rahul","age":18,"gender":"M"}
          ,{"id":2,"name":"harry","age":18,"gender":"M"}]
@app.get("/")
def first():
    return{
        "message":"lets start"
    }
@app.get("/data")
def get_request():
    return {
        "data":patients
    }
@app.post("/add_patient",status_code=status.HTTP_201_CREATED)
def post_request(data:data_request):
    for patient in patients:
        if data.id == patient["id"]:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Patient already exist"
            )
    patients.append(data.model_dump())
    return{
        "message":data
    }
@app.put("/change_data")
def put_request(data:data_request):
    for patient in patients:
        if data.id == patient["id"]:
            patient["name"]=data.name
            patient["age"]=data.age
            patient["gender"]=data.gender
            return{
                    "content":data
                }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )
@app.delete("/delete_patient/{patientId}",status_code=status.HTTP_200_OK)
def delete_request(patientId:int):
    for patient in patients:
            if patientId == patient["id"]:
                return{
                        "content":patient,
                        "details":"delete successfully"
                    }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"id not found"}
    )
@app.patch("/partial_patient/{patientId}",status_code=status.HTTP_200_OK)
def partial_update_request(patientId:int,data):
    for patient in patients:
            if patientId == patient["id"]:
                if data.name is not None:
                    patient["name"]=data.name
                if data.age is not None:
                    patient["age"]=data.age
                if data.gender is not None: 
                    patient["gender"]=data.gender
                return{
                        "content":patient,
                        "details":"update successfully"
                    }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"id not found"}
    )
