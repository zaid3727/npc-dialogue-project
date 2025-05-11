import os
import json
import nltk
from nltk.tokenize import sent_tokenize

from tqdm import tqdm

nltk.download('punkt')

BOOK_PATH = "data/Harry_Potter_all_books_preprocessed.txt"
CHUNK_SAVE_PATH = "data/book_chunks.json"
MAX_TOKENS = 300

def chunk_text(text):
    sentences = sent_tokenize(text)  # ✅ No manual model loading!
    chunks, current_chunk, current_len = [], [], 0

    for sent in sentences:
        tokens = sent.split()
        if current_len + len(tokens) > MAX_TOKENS:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_len = 0
        current_chunk.append(sent)
        current_len += len(tokens)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def process_book():
    with open(BOOK_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    structured_chunks = [{"text": chunk, "source": "book_corpus"} for chunk in chunks]

    with open(CHUNK_SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(structured_chunks, f, indent=2)

    print(f"✅ Saved {len(structured_chunks)} book chunks.")

if __name__ == "__main__":
    process_book()
