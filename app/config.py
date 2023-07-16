from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_hostname: str 
    database_port: str 
    database_password: str 
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str 
    access_token_expire_minute: int

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")

settings = Settings() #type: ignore