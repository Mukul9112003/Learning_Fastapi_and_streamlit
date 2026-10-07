users = {}


class Database:

    def __init__(self, database_name):
        self.database_name = database_name

    def create(self, data):
        users[data.id] = data

        return "User created successfully"

    def find_data(self):
        return users

    def find_data_by_id(self, user_id):
        return users.get(user_id)

    def update_data(self, user_id, data):
        users[user_id] = data

        return "User updated successfully"

    def delete_data(self, user_id):
        if user_id not in users:
            return None

        del users[user_id]

        return "User deleted successfully"

    def patch_data(self, user_id, data):

        existing_user = users.get(user_id)

        if existing_user is None:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():

            if key != "id":
                setattr(existing_user, key, value)

        return "User partially updated successfully"