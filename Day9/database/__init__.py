from database.factory import DatabaseFactory
from database.mongo.database import MongoDatabase
from database.sql.connection import get_sql_session
from database.sql.database import SQLDatabase

#from database.mongo.connection import get_mongo_connection


def create_sql_database():

    session = get_sql_session()

    return SQLDatabase(session)


'''def create_mongo_database():

    mongo = get_mongo_connection()

    return MongoDatabase(mongo)
'''

DatabaseFactory.register(
    "sql",
    create_sql_database
)

'''DatabaseFactory.register(
    "mongo",
    create_mongo_database
)
'''