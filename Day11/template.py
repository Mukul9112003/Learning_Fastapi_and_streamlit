from pathlib import Path

list_of_files=[
    "database",
    "database/database_connection.py"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    if not filepath.suffix:
        filepath.mkdir(parents=True,exist_ok=True)
    else:
        filepath.parent.mkdir(parents=True,exist_ok=True)
        filepath.touch(exist_ok=True)