import os
from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, load_prompt

# 1. Load Environment Variables
load_dotenv()

# 2. Configure Hugging Face Model
# We'll use Mistral-7B or Llama-3 as a powerful open-source alternative
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",  # Use this high-performing light model
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
)


model = ChatHuggingFace(llm=llm)

# 3. Streamlit UI
st.header('Research Tool')

paper_input = st.selectbox( 
    "Select Research Paper Name", 
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] 
)

style_input = st.selectbox( 
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] 
) 

length_input = st.selectbox( 
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] 
)

# 4. Load Template
# Ensure template.json exists in your 'langchain prompts' folder
template = load_prompt('template.json')

# 5. Execution Logic
if st.button('Summarize'):
    with st.spinner("Analyzing paper..."):
        chain = template | model
        result = chain.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        })
        
        st.subheader(f"Summary of {paper_input}")
        st.write(result.content)