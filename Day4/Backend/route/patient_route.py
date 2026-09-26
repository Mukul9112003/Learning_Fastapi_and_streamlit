from fastapi import APIRouter
from model.patient import patch_request_model, post_request_model, put_request_model
from services.service import (
    delete_patient_data,
    get_patient_data,
    get_patient_data_by_id,
    patch_patient_data,
    post_patient_data,
    put_patient_data,
)

patient=APIRouter()
@patient.get("/patient")
def get_patient():
    return {
        "message":get_patient_data()
    }
@patient.get("/patient/{id}")
def get_patient_by_id(id:int):
    return {
        "message":get_patient_data_by_id(id)
    }
@patient.post("/patient")
def post_patient(Data:post_request_model):
    return {
        "message":post_patient_data(Data)
    }
@patient.put("/patient/{id}")
def put_patient(id:int,Data:put_request_model):
    return {
        "message":put_patient_data(id,Data)
    }
@patient.patch("/patient/{id}")
def patch_patient(id:int,Data:patch_request_model):
    return {
        "message":patch_patient_data(id,Data)
    }
@patient.delete("/patient/{id}")
def delete_patient(id:int):
    return {
        "message":delete_patient_data(id)
    }