from src.interfaces.llm_service import LLMService


class FakeAIService(LLMService):

    def ask(self, messages):

        return "This is a fake response."

    def stream(self, messages):

        yield "This is a fake response."