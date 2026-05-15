# 🦜 LangChain Learning Hub

A centralized repository for exploring Large Language Model (LLM) orchestration, from foundational prompts to advanced serverless architectures. This hub demonstrates modular AI development using LangChain, Hugging Face, and Meta Llama models.

---

## 📂 Repository Structure

### 🏗️ [Advanced: Serverless Chat Architecture](./serverless-chat-architecture)
A production-ready conversational AI framework.
* **Key Features:** Stateful memory loops (System/Human/AI schemas), Decoupled serverless inference via Hugging Face API, and environment-secure credential handling.
* **Model:** Llama-3.2-1B-Instruct.

### 🧪 [Foundational Implementations](./foundations) 
*(Note: Use this if you have other folders for basic scripts)*
* **Concepts:** Basic Prompt Engineering, Chain-of-Thought logic, and Simple Memory Buffers.
* **Integrations:** Local Llama 3.2 (Ollama) and OpenAI GPT-4o wrappers.

---

## 🛠️ Tech Stack & Tools

* **Orchestration:** LangChain (`langchain-core`, `langchain-huggingface`)
* **Models:** Meta Llama 3.2, GPT-4o
* **Inference:** Hugging Face Inference API, Ollama (Local)
* **Environment:** Python 3.9+, Dotenv for security

---

## 🚀 Getting Started

1. **Clone the Hub:**
   ```bash
   git clone [https://github.com/uddeshya18/langchain-learning.git](https://github.com/uddeshya18/langchain-learning.git)
   cd langchain-learning
2. Configure Environment:
Each sub-project contains its own .env.example. Create a .env file in the relevant directory:


HUGGINGFACEHUB_API_TOKEN=your_token_here

3. Install Dependencies:


pip install -r requirements.txt
   
