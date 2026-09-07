from fastapi import FastAPI
from backend.database.database_connection import Base, engine
from backend.database.table import user
app=FastAPI(title="This is my api",version="1.0.0")
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{
        "message":"This is my home page"
    }
