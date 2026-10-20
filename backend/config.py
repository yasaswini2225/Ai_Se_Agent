import os
import json
from pathlib import Path
from pydantic import BaseModel
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
WORKSPACE_DIR = BASE_DIR / "workspace"
WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
SETTINGS_FILE = BASE_DIR / "settings.json"

class Settings(BaseModel):
    provider: str = "mock"  # "gemini", "openai", "groq", "ollama", "mock"
    gemini_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    groq_api_key: Optional[str] = None
    ollama_base_url: str = "http://localhost:11434"
    model_name: str = "gemini-2.5-flash"

def load_settings() -> Settings:
    # 1. Start with env vars
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    openai_key = os.environ.get("OPENAI_API_KEY", "")
    groq_key = os.environ.get("GROQ_API_KEY", "")
    provider = "gemini" if gemini_key else ("openai" if openai_key else "mock")
    model_name = "gemini-2.5-flash"
    ollama_url = "http://localhost:11434"

    # 2. Check settings.json
    if SETTINGS_FILE.exists():
        try:
            data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
            if data.get("provider"):
                provider = data["provider"]
            if data.get("gemini_api_key"):
                gemini_key = data["gemini_api_key"]
            if data.get("openai_api_key"):
                openai_key = data["openai_api_key"]
            if data.get("groq_api_key"):
                groq_key = data["groq_api_key"]
            if data.get("model_name"):
                model_name = data["model_name"]
            if data.get("ollama_base_url"):
                ollama_url = data["ollama_base_url"]
        except Exception:
            pass

    return Settings(
        provider=provider,
        gemini_api_key=gemini_key or None,
        openai_api_key=openai_key or None,
        groq_api_key=groq_key or None,
        ollama_base_url=ollama_url,
        model_name=model_name
    )

def save_persisted_settings(settings: Settings):
    data = {
        "provider": settings.provider,
        "gemini_api_key": settings.gemini_api_key or "",
        "openai_api_key": settings.openai_api_key or "",
        "groq_api_key": settings.groq_api_key or "",
        "ollama_base_url": settings.ollama_base_url,
        "model_name": settings.model_name
    }
    SETTINGS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

CURRENT_SETTINGS = load_settings()
