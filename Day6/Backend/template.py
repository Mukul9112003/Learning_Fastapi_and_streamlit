import os
from pathlib import Path

list_of_files=[
    "Database/data_base_connection.py",
    "routes/patientRoute.py",
    "services/PatientServices.py",
    "backend.py"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    if ( not os.path.exists(filepath)) or os.path.getsize(filepath)==0:
        with open(filepath,"a") as file:
            pass
    else:
        print(f"{filepath} exists")