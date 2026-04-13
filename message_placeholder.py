import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# 1. Load Environment
load_dotenv()

# 2. Setup Model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
)
model = ChatHuggingFace(llm=llm)

# 3. Define Template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# 4. Handle Chat History
# Note: Hugging Face needs objects, not raw lines of text
chat_history = []

# Mocking the load: usually, you'd parse your file into Human/AI messages
# For now, let's assume the file has alternating lines of history
try:
    with open('chat_history.txt') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 0:
                chat_history.append(HumanMessage(content=line.strip()))
            else:
                chat_history.append(AIMessage(content=line.strip()))
except FileNotFoundError:
    chat_history = [] # Fallback if file doesn't exist yet

# 5. Invoke Template & Model
prompt = chat_template.invoke({
    'chat_history': chat_history, 
    'query': 'Where is my refund'
})

result = model.invoke(prompt)
print(result.content)