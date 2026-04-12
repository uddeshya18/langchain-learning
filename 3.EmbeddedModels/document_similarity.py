from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Initialize local Hugging Face embeddings
# This model is free, fast, and runs entirely on your Mac
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat kohli is an indian cricketer known for his aggressive batting.",
    "Sachin Tendulkar is an indian cricketer famous for his handling skills.",
    "Rohit Sharma is an indian cricketer known for his fast bowling.",
    "MS Dhoni is an indian cricketer known for his captaincy.",
    "Anil Kumble is an indian cricketer known for his bowling skills."   
]

query = "Who is known for his captiancy?"

# 2. Generate embeddings
print("Generating embeddings...")
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# 3. Calculate Similarity
# We wrap query_embedding in [ ] because cosine_similarity expects a 2D array
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# 4. Find the best match
# We enumerate to keep track of the original index, then sort by score (descending)
results = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)

# Get the top result
index, score = results[0]

print("-" * 30)
print(f"Query: {query}")
print(f"Best Match: {documents[index]}")
print(f"Similarity Score: {score:.4f}")

# python 3.EmbeddedModels/document_similarity.py