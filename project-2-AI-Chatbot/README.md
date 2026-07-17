# 🤖 Professional AI Chatbot

A production-style command-line AI chatbot built using the OpenAI SDK with Google's Gemini API.

This project was developed as part of my AI Engineering Bootcamp to learn professional software architecture and modern LLM application development.

## ✨ Features

- Conversational AI powered by Gemini
- OpenAI SDK integration
- Streaming responses
- Conversation memory
- Configurable system prompts
- Professional project architecture
- Dependency Injection
- Factory Pattern
- Interface-based design
- Logging
- Unit Testing with pytest


                User
                  │
                  ▼
             ChatBot Layer
                  │
                  ▼
             AI Service
                  │
                  ▼
         Gemini (OpenAI SDK)


    project-2-ai-chatbot/

├── src/
│   ├── chatbot/
│   ├── config/
│   ├── factories/
│   ├── interfaces/
│   ├── prompts/
│   ├── services/
│   └── utils/
│
├── tests/
│
├── .env.example
├── pyproject.toml
├── uv.lock
└── README.md




## Installation

Clone the repository:

```bash
git clone <repository-url>

cd project-2-ai-chatbot
```

Install dependencies:

```bash
uv sync
```

## </>env

AI_PROVIDER=gemini

GEMINI_API_KEY=your_api_key_here

GEMINI_MODEL=gemini-2.5-flash

SYSTEM_PROMPT=You are a helpful AI assistant.




Run the chatbot:

```bash
uv run python src/main.py
```



🤖 Professional AI Chatbot

You:
What is Artificial Intelligence?

AI:
Artificial Intelligence (AI) is the field of computer science that focuses on building systems capable of performing tasks that typically require human intelligence...



