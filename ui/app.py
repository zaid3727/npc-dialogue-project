# ui/app.py

import streamlit as st
from src.retriever import retrieve_context
from src.prompt_builder import build_prompt, load_persona_config
from src.llm_interface import get_llm_response, extract_final_answer

st.set_page_config(page_title="Harry Potter NPC Chat", layout="centered")

st.title("🧙 Harry Potter NPC Chatbot")
st.markdown("Talk to your favorite characters. Responses are context-aware and in-character!")

# Load persona config
persona_config = load_persona_config()
npc_names = list(persona_config.keys())

# Sidebar
npc_name = st.sidebar.selectbox("Choose an NPC", npc_names)
user_query = st.text_input("Your Question", placeholder="e.g., What do you think about love?")

# Chat
if st.button("Ask"):
    if not user_query.strip():
        st.warning("Please enter a question.")
    else:
        # Retrieve and build prompt
        context_chunks = retrieve_context(npc_name, user_query, top_k=3)
        context_text = "\n".join([chunk["chunk"] for chunk in context_chunks])
        persona = persona_config[npc_name]
        prompt = build_prompt(npc_name, persona, context_text, user_query)

        # Get LLM response
        raw_response = get_llm_response(prompt)
        final_response = extract_final_answer(raw_response)

        # Display
        st.markdown(f"**{npc_name.replace('_', ' ').title()} says:**")
        st.info(final_response)

        with st.expander("📚 Show Retrieved Context"):
            st.code(context_text, language="text")

