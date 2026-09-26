from Database.database import patients
from exception.custom_exception import MyException


def get_patient_data():
    return patients
def get_patient_data_by_id(id):
    for patient in patients:
        if id<0:
            raise MyException("Invalid patient id")
        for patient in patients:
            if id == patient["id"]:
                return patient
    raise MyException("Patient not found")
def post_patient_data(post_data):
    if post_data.id < 0:
        raise MyException("Invalid patient id")
    for patient in patients:
        if post_data.id == patient["id"]:
            raise MyException("Duplicate patient id")
    patients.append(post_data.model_dump())
    return post_data
def put_patient_data(id:int,put_data):
    if id < 0:
        raise MyException("Invalid patient id")
    for patient in patients:
        if id == patient["id"]:
            patient["name"]=put_data.name
            patient["role"]=put_data.role
            patient["age"]=put_data.age
            return patient
    raise MyException("Patient not found")
def patch_patient_data(id,patch_data):
    if id < 0:
        raise MyException("Invalid patient id")
    for patient in patients:
        if id == patient["id"]:
            if patch_data.name in None:
                patient["name"]=patch_data.name
            if patch_data.role in None:
                patient["role"]=patch_data.role
            if patch_data.age in None:
                patient["age"]=patch_data.age
            return patient
    raise MyException("Patient not found")
def delete_patient_data(id:int):
    if id < 0:
        raise MyException("Invalid patient id")
    for patient in patients:
        if id == patient["id"]:
            patients.remove(patient)
    raise MyException("Patient not found")