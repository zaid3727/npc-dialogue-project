# src/embedder.py (or similar preprocessing script)

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 1: Chunk text with overlap
def chunk_text(text, chunk_size=300, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " "]
    )
    return splitter.split_text(text)

# Step 2: Process all NPCs and build FAISS index
def build_vector_store(npc_data_dir="npc_data", save_dir="data/vector_store"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    index = faiss.IndexFlatL2(384)  # 384 dims for MiniLM
    metadata = []

    for filename in os.listdir(npc_data_dir):
        if filename.endswith(".txt"):
            npc = filename.replace(".txt", "")
            with open(os.path.join(npc_data_dir, filename), "r", encoding="utf-8") as f:
                text = f.read()

            chunks = chunk_text(text)
            embeddings = embedding_model.encode(chunks)

            for i, embedding in enumerate(embeddings):
                index.add(embedding.reshape(1, -1))
                metadata.append({
                    "npc": npc,
                    "chunk": chunks[i]
                })

    # Save FAISS index
    faiss.write_index(index, os.path.join(save_dir, "npc.index"))

    # Save metadata
    with open(os.path.join(save_dir, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)

    print(f"✅ FAISS index built with {len(metadata)} chunks.")

if __name__ == "__main__":
    build_vector_store()
