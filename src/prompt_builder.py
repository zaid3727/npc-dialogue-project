import json
import os

# Path to persona config file
PERSONA_FILE = os.path.join(os.path.dirname(__file__), "../npc_data/persona_config.json")

def load_persona_config():
    with open("npc_data/persona_config.json", "r") as f:
        return json.load(f)


def build_prompt(character_name, persona, retrieved_chunks, user_query):
    tone = persona.get("tone", "neutral")
    quotes = "\n".join(f'- "{q}"' for q in persona.get("quotes", []))

    prompt = f"""
You are {character_name}, a fictional character from the Harry Potter universe.
You always speak in a way that reflects your tone: {tone}.
You are known for quotes like:
{quotes}

Use the following information to answer the user's question:

#CONTEXT:
{retrieved_chunks}

Before answering, think about the context, tone, and what you would say.

#SCRATCHPAD:
(Write your thoughts here.)

#ANSWER:
"""
    return prompt.strip()

# 🔧 Example test
if __name__ == "__main__":
    from retriever import retrieve_context

    persona_config = load_persona_config()
    npc = "hermione_granger"
    user_query = "What do you think about time travel?"
    chunks = retrieve_context(npc, user_query, top_k=3)
    persona = persona_config[npc]
    final_prompt = build_prompt(npc, persona, chunks, user_query)

    print("\n📜 Final Prompt:\n")
    print(final_prompt)
