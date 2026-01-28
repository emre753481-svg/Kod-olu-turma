from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "dev"
    app_name: str = "GitAnalyzer Pro"
    log_level: str = "INFO"

    github_token: str

    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    ai_provider: str = "openai"  # openai | anthropic

    plantuml_base_url: AnyHttpUrl = "https://www.plantuml.com/plantuml"
    frontend_origin: str = "http://localhost:5173"

settings = Settings()
