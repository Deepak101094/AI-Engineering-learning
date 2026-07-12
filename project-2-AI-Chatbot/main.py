from  src.chatbot.chatbot import Chatbot
from src.factories.llm_service_factory import LLMServiceFactory


def main():
    
    llm_service = LLMServiceFactory.create()

    chatbot = Chatbot(llm_service)

    chatbot.run()


if __name__ == "__main__":

    main()    




