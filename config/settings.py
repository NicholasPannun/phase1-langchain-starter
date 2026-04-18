import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    app_env: str = os.getenv("APP_ENV", "dev")
    model_provider: str = os.getenv("MODEL_PROVIDER", "ollama")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "orieg/gemma3-tools")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

settings = Settings()