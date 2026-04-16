from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Configurações base para o agente invisível B2A."""
    temporal_host: str = "localhost:7233"
    openai_api_key: str
    erp_webhook_secret: str
    llm_model: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
