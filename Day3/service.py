from Day3.data import patients
from Day3.custom_exception import MyException
from fastapi import HTTPException,status
def get_patients():
    return patients
def get_patients_by_id(number):
    if not patients:
        raise MyException("Database is empty")

    if number <= 0:
        raise MyException("Please enter valid id")

    for patient in patients:
        if patient["id"] == number:
            return patient

    raise MyException("Patient not found")
