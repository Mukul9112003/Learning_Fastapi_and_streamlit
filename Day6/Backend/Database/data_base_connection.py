from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session
DATABASE_URL="sqlite:///./text.db" 
engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
BASE=declarative_base()
SessionLocal=sessionmaker(bind=engine)
class patientTable(BASE):
    __tablename__="patient"
    id=Column(Integer,index=True,primary_key=True)
    name=Column(String)
    age=Column(Integer)
BASE.metadata.create_all(bind=engine)
def db_session():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
