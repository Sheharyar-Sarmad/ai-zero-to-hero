from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Application
    app_name: str = "PatchPilot"
    app_env: str = "development"
    debug: bool = True
    log_level: str = "INFO"

    # LLM
    groq_api_key: str

    low_model: str
    medium_model: str
    high_model: str

    llm_temperature: float = 0.1
    llm_max_tokens: int = 4096

    # PostgreSQL
    database_url: str
    
    # Google / Gmail
    google_client_id: str
    google_client_secret: str
    google_redirect_uri: str

    # Workflow
    max_workflow_iterations: int = 5
    workflow_timeout_seconds: int = 600

    # Security
    secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
