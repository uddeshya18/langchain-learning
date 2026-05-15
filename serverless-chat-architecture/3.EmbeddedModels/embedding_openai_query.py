from langchain_openai import OpenAIEmbeddings # Corrected capitalization
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Assign the instance to the variable 'embedding'
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large", 
    dimensions=32
)

# Now 'embedding' exists and can be used
result = embedding.embed_query("What is the capital of India?")

# Print the list of numbers (the vector)
print(result)

# python 3.EmbeddedModels/embedding_openai_query.py