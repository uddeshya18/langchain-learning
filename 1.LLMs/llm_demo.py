from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# 1. Verify API Key exists
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not found. Please ensure it is set in your .env file.")
else:
    # 2. Use ChatOpenAI for gpt-3.5-turbo (Chat models)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    try:
        print("Sending request to OpenAI...")
        result = llm.invoke("What is the capital of India?")
        
        # 3. ChatOpenAI returns a message object; use .content to get the text string
        print("\nResponse:")
        print(result.content)
    except Exception as e:
        print(f"\nAn error occurred during the API call: {e}")
