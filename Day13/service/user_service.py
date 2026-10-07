from repository.Base import BaseRepository


class UserService:

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def create_user(self, data):

        existing_user = self.repository.get_user_by_id(data.id)

        if existing_user:
            return {
                "message": "User already exists"
            }

        result = self.repository.create(data)

        return {
            "message": result
        }

    def get_users(self):

        data = self.repository.get_users()

        return {
            "data": list(data.values())
        }

    def get_user_by_id(self, user_id):

        data = self.repository.get_user_by_id(user_id)

        if data is None:
            return {
                "message": "User not found"
            }

        return {
            "data": data
        }

    def update_user(self, user_id, data):

        existing_user = self.repository.get_user_by_id(user_id)

        if existing_user is None:
            return {
                "message": "User not found"
            }

        result = self.repository.update_user(user_id, data)

        return {
            "message": result
        }

    def delete_user(self, user_id):

        existing_user = self.repository.get_user_by_id(user_id)

        if existing_user is None:
            return {
                "message": "User not found"
            }

        result = self.repository.delete_user(user_id)

        return {
            "message": result
        }

    def patch_user(self, user_id, data):

        existing_user = self.repository.get_user_by_id(user_id)

        if existing_user is None:
            return {
                "message": "User not found"
            }

        result = self.repository.patch_user(user_id, data)

        return {
            "message": result
        }