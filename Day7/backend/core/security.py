from jose import jwt,JWTError
from 
import os
from pathlib import Path
project="fastapi_lld"
filepaths=[
    f"{project}/.env"
]
for filepath in filepaths:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    if not (filename=="") or os.getsize(filename):
        with open(filepath,"a") as f:
            pass
    else:
        print("{pathpath} exists")