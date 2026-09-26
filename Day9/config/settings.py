import os


class Settings:

    database_url = os.getenv(
        "DATABASE_URL",
        "sqlite:///./users.db"
    )

    database_type = os.getenv(
        "DATABASE_TYPE",
        "sql"
    )


settings = Settings()