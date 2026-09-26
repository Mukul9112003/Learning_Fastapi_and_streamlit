from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    TOKEN_EXPIRE_MINUTES:int

    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
setting=Setting()
