import streamlit as st
import fitz  # PyMuPDF
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

# Extract text from PDF
def extract_questions_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    # Optional: split into individual questions
    questions = [q.strip() for q in text.split('\n') if q.strip()]
    return questions

# Call Ollama API to generate similar questions
def generate_similar_questions(original_questions, model="llama3"):
    prompt = f"""
You are an AI teacher. Given the following questions, generate 20 similar questions along with their answers.
Format:
Q1: <question>
A1: <answer>

Questions:
{original_questions}
"""
    response = requests.post(
        OLLAMA_URL,
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

# Streamlit UI
st.title("📘 AI-Powered Question Paper Augmenter")
st.write("Upload a question paper PDF. Get 20 similar questions with answers!")

pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

if pdf_file:
    questions = extract_questions_from_pdf(pdf_file)
    question_block = "\n".join(questions[:10])  # Use top 10 for prompt brevity
    st.write("### Extracted Questions")
    st.write(question_block)

    if st.button("Generate 20 Similar Questions"):
        with st.spinner("Generating..."):
            output = generate_similar_questions(question_block)
            st.success("Done!")
            st.text_area("Generated Questions & Answers", output, height=500)
