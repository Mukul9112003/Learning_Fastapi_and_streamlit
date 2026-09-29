from database.crud import CRUD


class UserPersistence:
    def __init__(self,database):
        collection=database.get_collection("user")
        self.crud=CRUD(collection)
    def create(self,user):
        return self.crud.create(user)
    def get_by_id(self,user_id):
        return self.crud.find_one({"_id":user_id})
    def get_by_email(self,email):
        return self.crud.find_one({"email":email})
    def get_all(self):
        return self.crud.find_many()
    def delete(self,email):
        return self.crud.delete_one({"email":email})