import os
from typing import List


class Settings:
    def __init__(self) -> None:
        api_provider: str = os.getenv("AI_PROVIDER", "mock").lower()
        self.ai_provider = api_provider  # mock | gemini | openai | groq | together

        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
        self.cors_allow_origins: List[str] = [frontend_url]

        # Optional third-party keys (not used by mock)
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.groq_api_key = os.getenv("GROQ_API_KEY", "")
        self.together_api_key = os.getenv("TOGETHER_API_KEY", "")


settings = Settings()


