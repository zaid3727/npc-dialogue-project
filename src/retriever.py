import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Paths
VECTOR_STORE = "data/vector_store"
INDEX_PATH = os.path.join(VECTOR_STORE, "npc.index")
METADATA_PATH = os.path.join(VECTOR_STORE, "metadata.json")

# Load model and data
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_PATH)

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

def retrieve_context(npc_name, user_query, top_k=3):
    query_vec = model.encode([user_query], convert_to_numpy=True)
    distances, indices = index.search(query_vec, top_k * 2)

    results = []
    for idx in indices[0]:
        chunk = metadata[idx]
        # prioritize either matching NPC or book corpus
        if chunk['npc'] == npc_name or chunk['npc'] == 'book_corpus':
            results.append(chunk)
        if len(results) >= top_k:
            break

    return results

