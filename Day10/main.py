from database.connection import DatabaseConnection
from fastapi import FastAPI
from persistence.user_persistence import UserPersistence

app = FastAPI()


database = DatabaseConnection(
    url="mongodb://localhost:27017",
    database_name="auth_app"
)

user_persistence = UserPersistence(database)


@app.post("/test-user")
def create_test_user():

    user = {
        "name": "Mukul",
        "email": "mukul@example.com"
    }

    user_id = user_persistence.create(user)

    return {
        "message": "User created",
        "user_id": str(user_id)
    }