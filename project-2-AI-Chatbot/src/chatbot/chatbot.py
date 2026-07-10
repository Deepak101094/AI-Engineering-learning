from src.services.gemini_service import GeminiService


class Chatbot:

    def __init__(self):
        
        self.gemini_service = GeminiService()


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


    def run(self):

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

                response = self.gemini_service.ask(
                    [
                        {
                            "role": "system",
                            "content": "You are a helpful assistant"
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                self.display_response(response)

            except Exception as e:

                print(f"\nError: {e}")    

