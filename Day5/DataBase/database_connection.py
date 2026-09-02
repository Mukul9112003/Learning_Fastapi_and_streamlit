from fastapi import FastAPI,Request,Depends
from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.orm import sessionmaker,declarative_base,Session
app=FastAPI()
DATABASE="sqlite:///./test.db" #"mysql+pymysql://root:your_password@localhost:3306/company_db"
engine=create_engine(DATABASE,connect_args={"check_same_thread":False})
sessionLocal=sessionmaker(bind=engine)
BASE=declarative_base()
class Todo(BASE):
    __tablename__="todo"
    id=Column(Integer,primary_key=True,index=False)
    title=Column(String)
    completed=Column(String)
BASE.metadata.create_all(bind=engine)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
