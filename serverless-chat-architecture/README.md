<<<<<<< HEAD
# 🦜🔗 LangChain Mastery
### Modular LLM & Embedding Implementation Hub

A technical repository demonstrating the core pillars of Agentic AI and RAG. This project serves as a documented guide for implementing LLMs, Chat-optimized models, and Vector Embeddings using both cloud APIs and local inference.

## 🚀 Key Modules

### 1. LLM Foundations (`/1.LLMs`)
* **Standard Completion:** Core logic for interfacing with base Large Language Models.
* **Orchestration:** Initializing predictable text-generation chains.

### 2. Conversational AI (`/2.ChatModels`)
* **Cloud Integration:** Production-ready scripts for **OpenAI** and **Hugging Face API**.
* **Local Inference:** Implementations for running models locally (`hf_local`) to optimize for privacy and cost.

### 3. Semantic Logic (`/3.EmbeddedModels`)
* **Document Similarity:** Algorithms for vector-based content matching.
* **Multi-Provider Embeddings:** Comparative implementations using OpenAI and Hugging Face local embeddings.

## 🛠️ Tech Stack
* **Language:** Python 3.9+ (90% of core logic)
* **Framework:** LangChain
* **Models:** Meta Llama 3.2, OpenAI GPT-4o, Hugging Face Open-Source models.

## ⚙️ Quick Start
1. **Clone & Install:**
   ```bash
   git clone [https://github.com/uddeshya18/langchain-mastery.git](https://github.com/uddeshya18/langchain-mastery.git)
   pip install -r requirements.txt

=======
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
>>>>>>> 03b65871058de335e3be41e5f23df6bd24c9e938
