import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate

# 1. Load your HUGGINGFACEHUB_API_TOKEN
load_dotenv()

# 2. Setup the Hugging Face Endpoint
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
)

# 3. Wrap it in ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# 4. Define your Template (Exactly as you had it!)
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

# 5. Invoke the template with variables
prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Doosra'})

# 6. Send the formatted prompt to the model
result = model.invoke(prompt)

print(result.content)