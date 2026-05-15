import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 1. Load your HUGGINGFACEHUB_API_TOKEN from .env
load_dotenv()

# 2. Setup the LLM (Using Llama-3.2 for better compatibility with chat history)
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
)

model = ChatHuggingFace(llm=llm)

# 3. Initialize Chat History
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

print("--- Chatbot Started (Type 'exit' to stop) ---")

# 4. Chat Loop
while True:
    user_input = input('You: ')
    
    if user_input.lower() == 'exit':
        break
        
    chat_history.append(HumanMessage(content=user_input))
    
    # Generate the response
    # ChatHuggingFace handles the conversion of messages to the model's format
    result = model.invoke(chat_history)
    
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print("\n--- Final Chat History ---")
print(chat_history)