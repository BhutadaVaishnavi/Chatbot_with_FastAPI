Project Overview
This project creates a FastAPI server that uses LangChain and Ollama models to generate short essays, poems for kids, and allow chatting with an AI model.

FastAPI:
Used to build a fast, simple, and high-performance web server for the API endpoints.
LangChain:
Makes it easy to connect prompts, models, and chains together, especially for complex LLM workflows.
Ollama / ChatOllama:
To run lightweight, powerful language models like LLaMA 3 locally without depending on external APIs.
LangServe:
Automatically creates API routes for LangChain chains and models, saving time on manual endpoint setup.
dotenv:
To load environment variables securely (like API keys or model configs) from a .env file.
Uvicorn:
A lightning-fast ASGI server to run the FastAPI app.

he server uses langserve to easily add AI model routes, and ChatOllama (configured for models like llama3) to handle the text generation tasks. Environment variables are managed securely with python-dotenv, and the application runs using uvicorn.
