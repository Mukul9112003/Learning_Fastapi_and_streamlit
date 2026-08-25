from fastapi import FastAPI,Depends,status,HTTPException,Request
from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base,Session
BASE=declarative_base()
DATABASE_URL="sqlite:///./test.db"
engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
SESSION_LOCAL=sessionmaker(bind=engine)
class Todo(BASE):
    id=Column(Integer,index=True,primary_key=True)
    name=Column(String)
BASE.metadata.create_all(bind=engine)
def db_session():
    db=SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()

app=FastAPI()
@app.middleware("http")
async def my_middleware(request:Request,call_next):
    response=await(call_next(request))
    return response
@app.get("/")
def get_method(data:Session=Depends(db_session)):
    return {
        "message":"Database created"
    }