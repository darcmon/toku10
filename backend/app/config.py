from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "Toku10 API"
    debug: bool = False
    database_url: Optional[str] = None
    secret_key: str = "your-secret-key-here"
    
    class Config:
        env_file = ".env"

settings = Settings()
