from pymongo import MongoClient
class DataBaseConnection:
    def __init__(self):
        self.database_url=MongoClient("mongodb://localhost:27017/")
        self.db=self.database_url["auth_app"]
    def get_collection(self,collection):
        return self.db[collection]
    def db_close(self):
        return self.database_url.close()