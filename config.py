from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )

    GROQ_API_KEY: str
    DATABASE_URL: str
    TAVILY_API_KEY: str
    AVIATIONSTACK_API_KEY: str

settings = Settings()