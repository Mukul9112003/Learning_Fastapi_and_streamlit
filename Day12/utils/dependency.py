from database.database_connection import DataBaseConnection
from repository.User.mongo_user_repository import MongoUserRepository
from service.UserServiceAuth import UserAuthService
database = DataBaseConnection()

repository = MongoUserRepository(database)

def get_user_service():
    return UserAuthService(repository)