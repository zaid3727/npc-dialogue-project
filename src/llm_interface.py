# src/llm_interface.py

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_NAME = "tiiuae/falcon-7b-instruct"

print("🔄 Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype="auto"
)

text_generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    do_sample=True,
    top_k=50,
    temperature=0.7,
    repetition_penalty=1.2
)

def get_llm_response(prompt: str) -> str:
    output = text_generator(prompt)[0]["generated_text"]
    return output[len(prompt):].strip()

def extract_final_answer(response_text):
    if "#ANSWER:" in response_text:
        return response_text.split("#ANSWER:")[-1].strip()
    return response_text.strip()

# 🧪 Example test
if __name__ == "__main__":
    example_prompt = """
You are Hermione Granger. Speak formally, intelligently, and with logical precision.
You are known for quotes like:
- "It's Leviosa, not Leviosar!"
- "Books! And cleverness!"

#CONTEXT:
Time-Turners are magical devices used for time travel. Misuse of them can cause major harm.

#SCRATCHPAD:
I know Hermione values rules and responsibility. She would warn against careless use of time travel.

#ANSWER:
"""

    raw = get_llm_response(example_prompt)
    final = extract_final_answer(raw)

    print("🤖 Final Answer:\n")
    print(final)
