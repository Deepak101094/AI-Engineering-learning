from src.services.gemini_service import GeminiService


def main():

    service = GeminiService()


    
    answer = service.ask(
        [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": "Introduce yourself in 5 line"
            }
        ]
    )
   
    # answer = service.ask("Introduce yourself in 5 line")

    print(answer)


if __name__ == "__main__":
    main()    




