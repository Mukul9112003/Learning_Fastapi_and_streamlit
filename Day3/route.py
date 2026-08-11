from fastapi import APIRouter
from Day3.service import get_patients,get_patients_by_id
mukul=APIRouter()
@mukul.get("/home")
def get_patient():
    return {
        "message":get_patients()
    }
@mukul.get("/home/{id}")
def get_patient_id(id:int):
    return {
        "message":get_patients_by_id(id)
    }