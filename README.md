# 🧙 Retrieval-Augmented NPC Dialogue Agents (Harry Potter Edition)

This project builds intelligent, character-driven NPCs using:
- 🔍 **Retrieval-Augmented Generation (RAG)**
- 🤖 **Large Language Models** (OpenAI GPT-3.5 / HuggingFace)
- 🎭 **Persona conditioning** to maintain tone and character consistency

---

## ✨ Use Case

Simulate realistic and grounded conversations with characters like Severus Snape, Hermione Granger, or Tom Riddle.  
The system uses character bios and quote data to ensure each NPC speaks in their canonical voice.

---

## 📁 Project Structure

```
npc_dialogue_project/
├── npc_data/        # Character bios + tone-defining quotes
├── data/            # FAISS vector index for semantic retrieval
├── src/             # Core logic: embedding, retrieval, prompt building
├── ui/              # Streamlit chatbot interface
├── eval/            # Evaluation rubric and scoring script
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the chatbot (Streamlit)
```bash
cd ui
streamlit run app.py
```

### 3. Run evaluation
```bash
python eval/evaluate.py
```

---

## 🧪 Evaluation Metrics

Each NPC response is scored using:
- ✅ **Grounding (0–2):** Based on retrieved context
- ✅ **Persona (0–2):** Matches expected character tone and personality
- ✅ **Hallucination (Yes/No):** Avoids made-up facts

Scores are stored in `eval/eval_rubric.csv`.  
Results are summarized with `eval/evaluate.py`.

---

## 📊 Included NPCs

| Character       | Traits                            |
|-----------------|-----------------------------------|
| 🧙 Severus Snape | Sarcastic, cold, emotionally complex |
| 📚 Hermione Granger | Logical, precise, confident      |
| 🧛‍♂️ Tom Riddle     | Charismatic, manipulative, dark    |
| ⚡ Harry Potter    | Brave, loyal, impulsive            |

You can add more characters by placing `.txt` files in `npc_data/`.

---

## 🧠 How It Works

1. **Load character documents** (bios + quotes)
2. **Embed and store** in FAISS vector store
3. **User inputs a query** → top-k chunks are retrieved
4. **Persona + context + question** form the final prompt
5. **LLM responds** in the character's voice

---

## 🔄 Supported Models

- 🟢 HuggingFace models (`mistral`, `flan-t5`, `llama-2`)
- Configurable in `src/llm_interface.py`

---

## 🧪 Example Interaction

**User:** Why did you hate Harry’s father?

**Snape (NPC):**  
*Your father was an arrogant, entitled show-off. Just like you. Always strutting around as if the world owed him something...*

---

## 📄 License

MIT License © 2025

---

## 🤝 Contributing

Pull requests are welcome. Add new characters, improve prompts, or extend the UI.  
Make sure to follow the project’s persona integrity guidelines.

---

## 🌐 Credits

Inspired by the [LLM Engineering Essentials](https://github.com/nebius/llm-engineering-essentials) course by Nebius Academy.

