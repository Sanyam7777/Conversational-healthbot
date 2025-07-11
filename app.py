# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12_qm3jn_r0ZCEICil83X2hob4EPIFOjq
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import fitz
# import re
# import torch
# import faiss
# import pickle
# from sentence_transformers import SentenceTransformer
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# 
# # Load RAG
# @st.cache_resource
# def load_rag():
#     with open("rag_index.pkl", "rb") as f:
#         index, chunks, embed_model = pickle.load(f)
#     return index, chunks, embed_model
# 
# rag_index, rag_chunks, embed_model = load_rag()
# 
# # Load FLAN-T5-LARGE model
# @st.cache_resource
# def load_model():
#     tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
#     model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large").to("cuda" if torch.cuda.is_available() else "cpu")
#     return tokenizer, model
# 
# tokenizer, model = load_model()
# 
# # RAG retrieval
# def retrieve_medical_context(question, k=2):
#     query_embedding = embed_model.encode([question])
#     _, indices = rag_index.search(query_embedding, k)
#     return "\n".join([rag_chunks[i] for i in indices[0]])
# 
# # Generate response
# def flan_t5_rag_answer(question):
#     context = retrieve_medical_context(question)
#     prompt = (
#         f"You are a medical assistant. Read the following trusted medical context and explain the answer in simple terms for a patient.\n\n"
#         f"Context:\n{context}\n\n"
#         f"Question: {question}\n\n"
#         f"Answer:"
#     )
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(model.device)
#     outputs = model.generate(**inputs, max_new_tokens=300)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)
# 
# # PDF text extraction
# def extract_text_from_pdf(pdf_file):
#     text = ""
#     with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
#         for page in doc:
#             text += page.get_text()
#     return text
# 
# # Medical term extraction
# def extract_medical_terms(text):
#     medical_terms = ['hemoglobin', 'ldl', 'hdl', 'creatinine', 'glucose', 'platelets',
#                      'cholesterol', 'vitamin d', 'tsh', 'bun', 'gfr', 'uric acid']
#     found_terms = {}
#     for term in medical_terms:
#         matches = re.findall(rf"{term}.*?[\d.]+", text, re.IGNORECASE)
#         if matches:
#             found_terms[term.lower()] = matches
#     return found_terms
# 
# # Streamlit UI
# st.title("🩺 Conversational Health Report Generator (Flan-T5-Large)")
# 
# uploaded_pdf = st.file_uploader("📄 Upload your PDF health report", type="pdf")
# 
# if uploaded_pdf:
#     with st.spinner("Extracting text..."):
#         raw_text = extract_text_from_pdf(uploaded_pdf)
#         st.subheader("📑 Extracted Report Text")
#         st.text_area("Text", raw_text, height=300)
# 
#         st.subheader("🧬 Key Medical Terms Found")
#         terms = extract_medical_terms(raw_text)
#         if terms:
#             for k, v in terms.items():
#                 st.write(f"**{k.upper()}**: {v}")
#         else:
#             st.info("No key medical terms found.")
# 
# # Chat interface
# st.subheader("💬 Ask a Question About Your Report")
# user_question = st.text_input("Example: What does high LDL mean?")
# 
# if user_question:
#     with st.spinner("🧠 Generating answer..."):
#         reply = flan_t5_rag_answer(user_question)
#         st.markdown(f"**🧠 Assistant:** {reply}")
#





