from database.crud import Database
from repository.Base import BaseRepository

class UserRepository(BaseRepository):

    def __init__(self):
        self.db = Database("users")

    def create(self, data):
        return self.db.create(data)

    def get_users(self):
        return self.db.find_data()

    def get_user_by_id(self, user_id):
        return self.db.find_data_by_id(user_id)

    def update_user(self, user_id, data):
        return self.db.update_data(user_id, data)

    def delete_user(self, user_id):
        return self.db.delete_data(user_id)

    def patch_user(self, user_id, data):
        return self.db.patch_data(user_id, data)