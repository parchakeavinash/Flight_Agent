from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    GROQ_API_KEY: str
    DATABASE_URL: str
    TAVILY_API_KEY: str
    AVIATIONSTACK_API_KEY: str

settings = Settings()
