class CRUD:
    def __init__(self,collection):
        self.collection=collection
    def create(self,data):
        result=self.collection.insert_one(data)
        return result.inserted_id
    def find_one(self,query):
        return self.collection.find_one(query)
    def find_many(self,query=None):
        if query is None:
            query={}
        return list(self.collection.find_many(query))
    def update_one(self,query,data):
        return self.collection.update_one(
            query,
            {"$set":data}
        )
    def delete_one(self,query):
        return self.collection.delete_one(query)