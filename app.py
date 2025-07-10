import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Gen AI Chatbot", layout="centered")
st.title("🧠 Gen AI Chatbot")

user_input = st.text_input("Ask me something:")

if user_input:
    with st.spinner("Generating response..."):
        gen = pipeline("text-generation", model="gpt2")
        result = gen(user_input, max_length=100, do_sample=True)
        st.write(result[0]['generated_text'])