from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import torch

print("Loading model... (This may take a few minutes on the first run)")

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512, 
        temperature=0.7,
        device=0 if torch.backends.mps.is_available() else -1 # Uses your Mac's GPU
    )
)

model = ChatHuggingFace(llm=llm)

print("Model loaded! Sending prompt...")
result = model.invoke("What is the capital of India?")

print("\nResponse:")
print(result.content)
