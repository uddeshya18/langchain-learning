import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 1. Load HUGGINGFACEHUB_API_TOKEN from your .env file
load_dotenv()

# 2. Initialize the LLM
# Using Llama-3.2-1B-Instruct as it's free and fast on the serverless API
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
)

# 3. Wrap it in ChatHuggingFace to handle the message history format
model = ChatHuggingFace(llm=llm)

# 4. Define your conversation
messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

# 5. Invoke the model
result = model.invoke(messages)

# 6. Append the AI's response to the history
messages.append(AIMessage(content=result.content))

# 7. Print the full history
print(messages)