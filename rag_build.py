from sentence_transformers import SentenceTransformer
import faiss
import pickle

# ✅ Use encoding fallback to handle weird characters
with open("med_sources.txt", "r", encoding="utf-8", errors="ignore") as f:
    chunks = [line.strip() for line in f if line.strip()]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(chunks)

# Build FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save everything
with open("rag_index.pkl", "wb") as f:
    pickle.dump((index, chunks, model), f)

print("✅ RAG index built and saved to rag_index.pkl.")
