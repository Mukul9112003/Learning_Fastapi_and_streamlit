class UserAuthService:

    def __init__(self, repository):
        self.repository = repository

    def register(self, user):

        existing_user = self.repository.get_by_email(user.email)

        if existing_user:
            return {
                "message": "User already exists"
            }

        user_id = self.repository.create(user)

        return {
            "message": "User registered",
            "user_id": str(user_id)
        }