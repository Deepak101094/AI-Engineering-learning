from src.config.settings import Settings
from src.services.gemini_service import GeminiService


class LLMServiceFactory:
    """
    Factory responsible for creating AI services.
    """

    @staticmethod

    def create():
        provider = Settings.AI_PROVIDER.lower()

        if provider == "gemini":
            return GeminiService()
        
        raise ValueError(
            f"Unsupported AI Provider: {provider}"
        )