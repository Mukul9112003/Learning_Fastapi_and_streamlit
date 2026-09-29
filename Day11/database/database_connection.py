from pymongo import MongoClient


class DatabaseConnection:
    def __init__(self,url:str,database_name:str):
        self.client=MongoClient(url)
        self.db=self.client[database_name]
    def get_collection(self,collection):
        return self.db[collection]
    def close(self):
        return self.client.close()
