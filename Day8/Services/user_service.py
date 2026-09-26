from repository.User.User import DataBase


class UserService:
    def __init__(self,db:DataBase):
        self.db=db
    def register(self,data):
        user=self.db.get_by_id(data["username"])
        if user:
            return "Already exist"
        hashed_password = data["password"]#hash_password(data["password"])
        user={"username":data["username"],"hassed_password":hashed_password}
        message=self.db.save_data(user)
        return message