from redis.asyncio import Redis
from fastapi import FastAPI
import json
from database.database_connection import DatabaseConnection
from persistence.user_persistence import UserPersistence
app=FastAPI(title="Backend ")
database=DatabaseConnection(
    url="mongodb://localhost:27017",
    database_name="auth_app"
)
user_persistence=UserPersistence(database)

redis_client=Redis(
    host="localhost",port=6379,decode_responses=True
)
@app.post("/test-user")
async def create_test_user():
    user={
        "name":"Mukul",
        "email":"mukul@example.com"
    }
    user_id=user_persistence.create(user)
    await redis_client.set(f"user:{str(user_id)}",json.dumps(user),ex=60)
    return{
        "message":"User created",
        "user_id":str(user_id)
    }
