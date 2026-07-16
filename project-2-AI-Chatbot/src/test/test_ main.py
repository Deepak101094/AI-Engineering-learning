from src.chatbot.chatbot import Chatbot
from src.test.test_chatbot import FakeAIService


def test_chatbot_creation():

    service = FakeAIService()

    chatbot = Chatbot(service)

    assert chatbot is not None