import os
import json

# Persona instructions per NPC
PERSONA_TEMPLATES = {
    "harry_potter": "You are Harry Potter. Speak bravely, kindly, and with modesty.",
    "hermione_granger": "You are Hermione Granger. Speak formally, intelligently, and with logical precision.",
    "severus_snape": "You are Severus Snape. Speak curtly, with sarcasm and authority.",
    "tom_riddle": "You are Tom Riddle. Speak cunningly, intelligently, and with a chilling calm.",
    # Add more if needed
}

def build_prompt(npc_name, context_chunks, user_query):
    persona = PERSONA_TEMPLATES.get(npc_name.lower())
    if not persona:
        raise ValueError(f"No persona defined for NPC: {npc_name}")

    context_text = "\n\n".join(chunk['text'] for chunk in context_chunks)

    prompt = (
        f"{persona}\n\n"
        f"Based on the following context:\n{context_text}\n\n"
        f"Answer the following question as the character:\n{user_query}"
    )
    return prompt

# 🔧 Example test
if __name__ == "__main__":
    # Simulate retrieved context from retriever.py
    from retriever import retrieve_context

    npc = "hermione_granger"
    user_query = "What do you think about time travel?"

    chunks = retrieve_context(npc, user_query, top_k=3)

    final_prompt = build_prompt(npc, chunks, user_query)

    print("\n📜 Final Prompt:\n")
    print(final_prompt)
