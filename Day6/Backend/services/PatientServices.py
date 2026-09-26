from customException.exc import MyException
from Database.data_base_connection import patientTable
from sqlalchemy.orm import Session


def patient_create(data,db:Session):
    table=patientTable(
        name=data.name,
        age=data.age
    )
    db.add(table)
    db.commit()
    db.refresh(table)
    return "data created successfully"
def getAllPatient(db:Session):
    table=db.query(patientTable).all()
    return table
def putPatient(data,id:int,db:Session):
    table=db.query(patientTable).filter(patientTable.id==id).first()
    if not table:
        raise MyException("No such patient found")
    table.name=data.name
    table.age=data.age
    db.commit()
    db.refresh(table)
    return "Successfully update "
def patchPatient(data,id:int,db:Session):
    table=db.query(patientTable).filter(patientTable.id==id).first()
    if not table:
        raise MyException("No such patient found")
    if data.name:
        table.name=data.name
    if data.age:
        table.age=data.age
    db.commit()
    db.refresh(table)
    return "Succussfully update using patch request"
def deletePatient(id,db:Session):
    table=db.query(patientTable).filter(patientTable.id==id).first()
    if not table:
        raise MyException("Id not found")
    db.delete(table)
    db.commit()
    db.refresh(table)