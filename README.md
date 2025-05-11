# Retrieval-Augmented Dialogue Agents (Harry Potter NPCs)

This project builds intelligent NPCs (e.g., Harry Potter characters) using:
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- OpenAI GPT-3.5 or HuggingFace LLMs
- Persona and tone preservation

## Structure
- `npc_data/`: Character bios and quotes
- `src/`: Code for embedding, retrieval, LLM prompt building
- `eval/`: Evaluation rubric and score templates
- `ui/`: Streamlit chatbot app

## Requirements
- Python 3.9+
- `sentence-transformers`, `faiss-cpu`, `openai`, `streamlit`, `transformers`

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
cd ui
streamlit run app.py
```

## Evaluate
```bash
python eval/evaluate.py
```
