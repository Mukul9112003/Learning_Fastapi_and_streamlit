from Database.data_base_connection import db_session
from fastapi import APIRouter, Depends
from services.PatientServices import (
    deletePatient,
    getAllPatient,
    patchPatient,
    patient_create,
    putPatient,
)
from sqlalchemy.orm import Session
from validation.patient_validation import patient_create_request_model

patient=APIRouter()

@patient.post("/create")
def create_service(data:patient_create_request_model,db:Session=Depends(db_session)):
    return {"message":patient_create(data,db)}
@patient.get("/getall")
def get_service(db:Session=Depends(db_session)):
    return {"data":getAllPatient(db)}
@patient.put("/update_patient_info/{id}")
def put_service(data:patient_create_request_model,id:int,db:Session=Depends(db_session)):
    return {"data":putPatient(data,id,db)}
@patient.patch("/update_patient_info/{id}")
def patch_service(data,id:int,db:Session=Depends(db_session)):
    return {"data":patchPatient(data,id,db)}
@patient.delete("/delete_patient/{id}")
def delete_service(id:int,db:Session=Depends(db_session)):
    return {"data":deletePatient(id,db)}