from dotenv import load_dotenv
import os
from google import genai



def load_api_key():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env")
    
    return api_key



def create_client(api_key):
    return genai.Client(api_key=api_key)



def ask_gemini(client, prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    return response.text


def chat(client):
    """
    Interactive chat loop with Gemini!.
    """

    print("Hello ! I'm gemini")
    print("Type 'exit' to quit.\n")

    while True:

        prompt = input("You: ")

        if not prompt.strip():
            print("Please enter a question.\n")
            continue

        if prompt.lower() == "exit":
            print("\n Goodbye")
            break

        try:
            response = ask_gemini(client, prompt)
            print(f"\n Gemini: {response} \n")
            print("--------------------------------")

        except Exception as e:
            print(f"\n Error{e}\n")
      



def main():

    api_key = load_api_key()

    client = create_client(api_key)

    chat(client)

   



if __name__ == "__main__":
    main()





