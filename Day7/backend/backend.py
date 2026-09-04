from fastapi import FastAPI
from routes.route import user
from database.database_connection import engine, Base
from database.Model import User
app=FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user)