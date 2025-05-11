import os
import glob
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_DIR = "npc_data"
OUTPUT_DIR = "data/vector_store"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_chunks():
    chunks = []
    metadata = []

    # Load NPC bios from txt files
    for filepath in glob.glob(os.path.join(DATA_DIR, "*.txt")):
        name = os.path.splitext(os.path.basename(filepath))[0]
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read().strip()
            if not text:
                continue
            paragraphs = text.split("\n\n")
            for i, para in enumerate(paragraphs):
                if len(para.split()) < 30:
                    continue
                chunks.append(para)
                metadata.append({
                    "npc": name,
                    "chunk_id": f"{name}_{i}",
                    "text": para
                })

    # Load book corpus chunks
    book_path = "data/book_chunks.json"
    if os.path.exists(book_path):
        with open(book_path, "r", encoding="utf-8") as f:
            book_chunks = json.load(f)
            for i, chunk in enumerate(book_chunks):
                text = chunk.get("text", "").strip()
                if len(text.split()) < 30:
                    continue
                chunks.append(text)
                metadata.append({
                    "npc": "book_corpus",
                    "chunk_id": f"book_{i}",
                    "text": text
                })

    return chunks, metadata


def build_and_save_index():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunks, metadata = load_chunks()

    if not chunks:
        print("❌ No chunks found. Please check your .txt files.")
        return

    embeddings = model.encode(chunks, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, os.path.join(OUTPUT_DIR, "npc.index"))

    with open(os.path.join(OUTPUT_DIR, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"✅ Saved FAISS index with {len(chunks)} entries.")

if __name__ == "__main__":
    build_and_save_index()
