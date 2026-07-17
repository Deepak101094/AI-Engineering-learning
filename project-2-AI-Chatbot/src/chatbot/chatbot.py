from src.services.gemini_service import GeminiService
from src.utils.logger import logger
from src.interfaces.llm_service import LLMService
from src.config.settings import Settings


class Chatbot:

    def __init__(self, ai_service: LLMService):
        
        self.ai_service = ai_service

        self.conversation_history = [
            {
                "role": "system",
                "content": Settings.SYSTEM_PROMPT
            }
        ]


    def display_welcome_message(self):

         """
        Display welcome message.
        """

         print("=" * 50)
         print("🤖 Welcome to Professional AI Chatbot")
         print("Type 'exit' to quit.")
         print("=" * 50)   


    def get_user_input(self):

        return input("\n You: ")
    

    def display_response(self, response):

        print(f"\n🤖 Gemini:\n")

        print(response)


    def stream_response(self):
         """
         Stream the assistant response and save it to conversation history.
         """    
         
         stream =  self.ai_service.stream(self.conversation_history)

         full_response = ""

         print("\n🤖 Gemini:\n")

         for chunk in stream:
             content = chunk.choices[0].delta.content

             if content:
                 print(content, end="", flush=True)
                 full_response += content

             print()


             self.conversation_history.append(
                 {
                     "role": "assistant",
                     "content": full_response
                 }
             )   


    def run(self):
        
        logger.info("Chatbot started.")
        self.display_welcome_message()

        while True:

            prompt = self.get_user_input()

            if prompt.lower() == "exit":

                print("\n👋 Goodbye")

                break

            if not prompt.strip():

                print("Please enter a prompt.")

                continue


            try: 
                
                logger.info(f"User Prompt: {prompt}")

                self.conversation_history.append(
                    {
                        "role": "user",
                        "content": prompt
                    }
                )

                self.stream_response()

                logger.info("Response generated successfully.")


            except Exception as e:

                print(f"\n❌ Error: {e}")

                logger.error(str(e))    

