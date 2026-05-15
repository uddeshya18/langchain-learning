🤖 Serverless LLM Chatbot
Architecture: LangChain + Meta Llama 3.2 + Hugging Face API

🎯 Overview
A stateful conversational AI implemented with a serverless architecture. This project focuses on contextual memory management and API-driven inference, demonstrating how to build scalable AI applications without local hardware dependencies.

🏗️ Technical Highlights
Stateful Orchestration: Implemented a persistent chat_history loop using LangChain’s SystemMessage, HumanMessage, and AIMessage schemas to maintain multi-turn dialogue context.

Serverless Inference: Integrated Hugging Face Inference API to serve Llama-3.2-1B-Instruct, optimizing for low-latency responses and decoupled compute.

Message Prompt Engineering: Utilized structured system prompting to define model behavior and constraints within a managed environment.

Environment Security: Built with python-dotenv to ensure secure handling of API credentials and adherence to production security standards.

🛠️ Tech Stack
LLM Framework: LangChain (langchain-huggingface)

Model: Meta Llama-3.2-1B-Instruct

Inference Provider: Hugging Face API

Environment: Python 3.9+ / Dotenv

🚀 Key Features
Short-Term Memory: Remembers previous interactions for coherent, human-like follow-up responses.

Scalable Backend: Easily swappable repo_id allows for testing larger parameter models (e.g., Llama-3 70B) with zero code changes.

Lightweight Deployment: Optimized for fast execution and minimal dependency bloat.
