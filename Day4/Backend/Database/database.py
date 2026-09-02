patients=[
    {"id":1,"name":"A","age":20,"role":"A"},
    {"id":2,"name":"B","age":20,"role":"A"},
    {"id":3,"name":"C","age":20,"role":"A"},
]
from fastapi import FastAPI,HTTPException,Request
from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.orm import declarative_base,sessionmaker,Session
DATABASE="localhost:8086:/company_db"
engine=create_engine(DATABASE,connect_args={"check_same_thread":False})
sessionLocal=sessionmaker(bind=engine)
BASE=declarative_base()
class Table(BASE):
    id=Column(Integer,index=False,primary_key=True)
    name=Column(String)
    age=Column(Integer)
BASE.metadata.create_all(bind=engine)
def session():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()