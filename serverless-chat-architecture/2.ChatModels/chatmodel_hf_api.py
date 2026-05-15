from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

# 1. Load environment variables
load_dotenv()

# 2. Setup the Model
try:
    # Llama-3.2-1B is highly compatible with the free API
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-1B-Instruct",
        task="text-generation",
        max_new_tokens=512,
    )
    
    model = ChatHuggingFace(llm=llm)

    print("Sending request to Hugging Face...")
    result = model.invoke("What is the capital of India?")
    
    print("\nResponse:")
    print(result.content)

except Exception as e:
    print(f"\nAn error occurred: {e}")