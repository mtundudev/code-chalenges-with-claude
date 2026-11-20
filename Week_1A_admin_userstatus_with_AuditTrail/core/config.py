from pydantic_settings import BaseSettings,SettingsConfigDict



class Settings(BaseSettings):
    DATABASE_URL:str
    JWT_SECRET:str
    ALGORITHM:str
    EXPIRE_ACCESS_TOKEN:int


    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings=Settings()

