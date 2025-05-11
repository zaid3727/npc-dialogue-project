from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# 🔧 Change to any instruct-tuned local model (must support chat-style prompts)
MODEL_NAME = "tiiuae/falcon-7b-instruct"

print("🔄 Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype="auto"  # Use float16 if supported
)

# Initialize generation pipeline
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
    # Strip the input prompt from the beginning of the response
    return output[len(prompt):].strip()

# 🧪 Example test
if __name__ == "__main__":
    example_prompt = """You are Hermione Granger. Speak formally, intelligently, and with logical precision.

Based on the following context:
Time-Turners are magical devices used for time travel, regulated by the Ministry of Magic. Misuse of them can result in catastrophic consequences.

Answer the following question as the character:
What do you think about death?"""

    print("🤖 Response:\n")
    print(get_llm_response(example_prompt))
