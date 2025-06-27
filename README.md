# Conversational Health Report Generator

The Conversational Health Report Generator is an AI-powered tool designed to help individuals understand their medical reports. It allows users to upload health-related PDFs (such as lab reports), extract key medical terms, and ask natural language questions about the report. The system responds with simplified, grounded explanations based on curated medical knowledge.

This project uses open-source large language models and retrieval-augmented generation (RAG) to provide accurate, human-friendly health insights — completely offline and without relying on proprietary APIs.

---

## Features

- Upload any text-based medical PDF report
- Automatically extract key medical indicators such as LDL, hemoglobin, glucose, vitamin D, and more
- Chat with a natural language interface to ask questions about medical terms or report contents
- Uses retrieval-augmented generation (RAG) to search a trusted local medical knowledge base
- Generates grounded, conversational explanations using `flan-t5-large` (a free, open-source language model)
- Designed for privacy and offline use — no internet-dependent APIs or external queries

---

## Example Use Cases

- Upload your blood test results and ask:  
  - "What does high LDL mean?"  
  - "Should I worry about low vitamin D?"  
  - "Is my hemoglobin normal?"

- The system will search your report, retrieve facts from trusted medical sources, and give a simple explanation.

---

## How It Works

1. The user uploads a medical report in PDF format
2. The system extracts raw text from the report using PyMuPDF
3. A set of predefined medical terms is identified (e.g., LDL, glucose, TSH)
4. The user can enter natural language questions
5. The system retrieves relevant medical context from a curated `.txt` knowledge base using FAISS and sentence transformers
6. The question and retrieved context are passed to the `flan-t5-large` model to generate an answer

---

## How to Run the Project

### 1. Clone this repository

```bash
git clone https://github.com/Sanyam7777/Conversational-healthbot.git
cd Conversational-healthbot
pip install -r requirements.txt
python rag_build.py
streamlit run app.py
