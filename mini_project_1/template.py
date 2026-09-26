from pathlib import Path

project = "mini_project_1/fastapi_lld"

filepaths = [
    f"{project}/.env",

    # App
    f"{project}/app/main.py",

    # Models
    f"{project}/app/models/user.py",

    # Schemas
    f"{project}/app/schemas/user.py",

    # Repositories
    f"{project}/app/repositories/user_repository.py",
    f"{project}/app/repositories/sql_user_repository.py",
    f"{project}/app/repositories/mongo_user_repository.py",

    # Services
    f"{project}/app/services/user_service.py",

    # Database
    f"{project}/app/database/sql_database.py",
    f"{project}/app/database/mongo_database.py",

    # Dependencies
    f"{project}/app/dependencies/repository.py",

    # Tests
    f"{project}/tests/test_user_service.py",
    f"{project}/tests/fake_user_repository.py",

    # Project files
    f"{project}/requirements.txt",
    f"{project}/README.md",
]

for filepath in filepaths:
    filepath = Path(filepath)

    # Create parent directories
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Create file if it doesn't exist
    if not filepath.exists():
        filepath.touch()
        print(f"Created: {filepath}")
    else:
        print(f"{filepath} already exists")