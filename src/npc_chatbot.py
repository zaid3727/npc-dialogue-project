# npc_chatbot.py

from retriever import retrieve_context
from prompt_builder import build_prompt
from llm_interface import get_llm_response

def chat_with_npc(npc_name: str, user_query: str, k: int = 3):
    # Step 1: Retrieve top-k relevant context chunks for the NPC
    context_chunks = retrieve_context(npc_name, user_query, top_k=k)

    # Step 2: Build a full prompt using persona and context
    prompt = build_prompt(npc_name, context_chunks, user_query)

    # Step 3: Generate response from the LLM
    response = get_llm_response(prompt)
    return response


# 🧪 Example
if __name__ == "__main__":
    npc = "Tom Riddle"
    question = "What do you think about death?"

    print(f"\n🧙 Talking to: {npc}")
    print(f"❓ Question: {question}")

    answer = chat_with_npc(npc, question)
    print("\n🤖 Response:")
    print(answer)
