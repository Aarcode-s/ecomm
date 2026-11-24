from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name :str = "E-Commerce API"
    version : str = "1.0.0"
    description : str = "this is a simple ecommerce API buit with FastAPI."
    environment :str = "Development"


    database_url: str
    secret_key :str 
    access_token_minutes: int = 15
    refresh_token_days: int = 14
    cors_origins: str   
    frontend_url: str = "http://localhost:5173"


    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

settings = Settings()  # pyright: ignore[reportCallIssue]