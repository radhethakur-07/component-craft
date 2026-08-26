from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import logging

# Configure basic logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

class Settings(BaseSettings):
    """
    Application configuration managed by Pydantic.
    It will automatically throw a rich error if an env var is missing.
    """
    PROJECT_NAME: str = "Component Craft AI"
    API_V1_STR: str = "/api/v1"
    
    # 🔒 SECRETS (Do NOT hardcode values here!)
    # Pydantic will automatically load these from the .env file or environment variables.
    SUPABASE_URL: str
    SUPABASE_KEY: str
    GEMINI_API_KEY: str
    
    # Search for .env file in the parent directories
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

@lru_cache()
def get_settings() -> Settings:
    """
    Uses LRU cache so we don't read the .env file multiple times.
    Singleton pattern for settings.
    """
    return Settings()

settings = get_settings()
logger = logging.getLogger(settings.PROJECT_NAME)