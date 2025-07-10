# app.py
import streamlit as st
from transformers import pipeline

st.title("🧠 Gen AI Chatbot")

question = st.text_input("Ask a question:")
if question:
    generator = pipeline("text-generation", model="gpt2")
    response = generator(question, max_length=100, do_sample=True)[0]['generated_text']
    st.write(response)