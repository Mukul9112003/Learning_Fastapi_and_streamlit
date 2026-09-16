from dotenv import load_dotenv
import os
from dataclasses import dataclass
load_dotenv()
@dataclass
class Setting:
    Secret_key:str|None=os.getenv("SECRET_KEY")
    DataBase_url:str|None=os.getenv("DATABASE_URL")
    Algorithm:str|None=os.getenv("ALGORITHM")
setting=Setting()