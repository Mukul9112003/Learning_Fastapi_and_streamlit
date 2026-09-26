from backend.database.database_connection import Base, engine
from fastapi import FastAPI

app=FastAPI(title="This is my api",version="1.0.0")
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{
        "message":"This is my home page"
    }
