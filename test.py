# ============================================================
# Database/databaseconnection.py
# ============================================================

from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pwdlib import PasswordHash
from pydantic import BaseModel
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

# ============================================================
# Database/databaseconnection.py
# ============================================================

class Base(DeclarativeBase):
    pass


DatabaseUrl = "sqlite:///./test.db"

engine = create_engine(
    DatabaseUrl,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)


def db_session():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ============================================================
# Model/UserTable.py
# ============================================================

class User(Base):

    __tablename__ = "user"

    username: Mapped[str] = mapped_column(
        String(100),
        primary_key=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255)
    )


# ============================================================
# Registry/database/user.py
# ============================================================

class Database(ABC):

    @abstractmethod
    def create_user(self, username, hashed_password):
        pass

    @abstractmethod
    def get_user(self, username):
        pass


# ============================================================
# Registry/database/sql_user.py
# ============================================================

class SQLDatabase(Database):

    def __init__(self, session: Session):
        self.session = session

    def create_user(self, username, hashed_password):

        statement = select(User).where(
            User.username == username
        )

        user = self.session.scalar(statement)

        if user:
            return None

        user = User(
            username=username,
            hashed_password=hashed_password
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def get_user(self, username):

        statement = select(User).where(
            User.username == username
        )

        return self.session.scalar(statement)


# ============================================================
# Schema/user.py
# ============================================================

class RegisterRequest(BaseModel):

    username: str
    password: str


class LoginRequest(BaseModel):

    username: str
    password: str


# ============================================================
# Service/password.py
# ============================================================

class PasswordService:

    def __init__(self):

        self.password_hash = PasswordHash.recommended()

    def hash_password(self, password):

        return self.password_hash.hash(password)

    def verify_password(
        self,
        password,
        hashed_password
    ):

        return self.password_hash.verify(
            password,
            hashed_password
        )


# ============================================================
# Service/token.py
# ============================================================

class TokenService:

    SECRET_KEY = "change-this-secret-key"

    ALGORITHM = "HS256"

    def create_token(self, username):

        expire = (
            datetime.now(timezone.utc)
            + timedelta(minutes=30)
        )

        payload = {
            "sub": username,
            "exp": expire
        }

        return jwt.encode(
            payload,
            self.SECRET_KEY,
            algorithm=self.ALGORITHM
        )

    def verify_token(self, token):

        try:

            payload = jwt.decode(
                token,
                self.SECRET_KEY,
                algorithms=[self.ALGORITHM]
            )

            username = payload.get("sub")

            if username is None:
                return None

            return username

        except JWTError:

            return None


# ============================================================
# Service/user.py
# ============================================================

class UserService:

    def __init__(
        self,
        database,
        password_service,
        token_service
    ):

        self.database = database
        self.password_service = password_service
        self.token_service = token_service

    def register(self, data):

        hashed_password = (
            self.password_service.hash_password(
                data.password
            )
        )

        return self.database.create_user(
            data.username,
            hashed_password
        )

    def login(self, data):

        user = self.database.get_user(
            data.username
        )

        if user is None:
            return None

        password_valid = (
            self.password_service.verify_password(
                data.password,
                user.hashed_password
            )
        )

        if not password_valid:
            return None

        return self.token_service.create_token(
            user.username
        )


# ============================================================
# main.py
# ============================================================

Base.metadata.create_all(bind=engine)

app = FastAPI()


# ============================================================
# JWT SECURITY
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


# ============================================================
# GET CURRENT USER
#
# This function protects endpoints.
# ============================================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(db_session)
):

    # Create TokenService
    token_service = TokenService()

    # Verify JWT
    username = token_service.verify_token(token)

    # Token is invalid
    if username is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    # Find user in database
    database = SQLDatabase(db)

    user = database.get_user(username)

    # User doesn't exist
    if user is None:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


# ============================================================
# REGISTER ENDPOINT
# ============================================================

@app.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(db_session)
):

    database = SQLDatabase(db)

    password_service = PasswordService()

    token_service = TokenService()

    user_service = UserService(
        database,
        password_service,
        token_service
    )

    user = user_service.register(data)

    if user is None:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return {
        "message": "User registered successfully",
        "username": user.username
    }


# ============================================================
# LOGIN ENDPOINT
# ============================================================

@app.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(db_session)
):

    database = SQLDatabase(db)

    password_service = PasswordService()

    token_service = TokenService()

    user_service = UserService(
        database,
        password_service,
        token_service
    )

    token = user_service.login(data)

    if token is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ============================================================
# PROTECTED ENDPOINT
# ============================================================

@app.get("/profile")
def profile(
    current_user: User = Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "username": current_user.username
    }