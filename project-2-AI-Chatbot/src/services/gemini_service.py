from openai import OpenAI

from src.config.settings import Settings
from src.interfaces.llm_service import LLMService

gemini_client = OpenAI(
    api_key= Settings.GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


class GeminiService(LLMService):
    """
    Handles communication with Gemini.
    """

    def __init__(self):

        self.client = gemini_client

        self.model = Settings.GEMINI_MODEL


    def ask(self, messages):

        response = self.client.chat.completions.create(
            model = self.model,
            messages = messages
        )

        return response.choices[0].message.content    


    def stream(self, messages):

         """
         Send a prompt to Gemini and return the response.
         """

         return self.client.chat.completions.create(
             model= self.model,
             messages = messages,
             stream= True
         )

         


