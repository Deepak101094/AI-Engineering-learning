from  src.chatbot.chatbot import Chatbot
from src.services.gemini_service import GeminiService

def main():
    
    service = GeminiService()

    chatbot = Chatbot(service)

    print(f"\nChatbot: {chatbot}")

    chatbot.run()


if __name__ == "__main__":

    main()    




