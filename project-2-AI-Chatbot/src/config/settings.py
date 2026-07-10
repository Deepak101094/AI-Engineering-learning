import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    """ 

    Application settings.
    """

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    if not GEMINI_API_KEY:
        raise ValueError(
             "GEMINI_API_KEY is missing. Please check your .env file."
        )
    
    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    APP_NAME = os.getenv(
        "APP_NAME",
        "Professional AI Chatbot"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )