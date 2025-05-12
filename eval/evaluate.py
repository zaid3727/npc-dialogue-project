import pandas as pd

def evaluate(file_path="eval/eval_rubric.csv"):
    df = pd.read_csv(file_path)

    # Clean up missing data
    df = df.dropna(subset=["Grounded(0-2)", "Persona(0-2)", "Hallucinated(Yes/No)"])

    # Convert types
    df["Grounded(0-2)"] = df["Grounded(0-2)"].astype(int)
    df["Persona(0-2)"] = df["Persona(0-2)"].astype(int)
    df["Hallucinated(Yes/No)"] = df["Hallucinated(Yes/No)"].str.lower()

    # Compute metrics
    grounded_avg = df["Grounded(0-2)"].mean()
    persona_avg = df["Persona(0-2)"].mean()
    hallucination_rate = (df["Hallucinated(Yes/No)"] == "yes").mean() * 100

    # Output
    print("📊 Evaluation Summary:")
    print(f"🔹 Avg Grounding Score: {grounded_avg:.2f} / 2")
    print(f"🔹 Avg Persona Score: {persona_avg:.2f} / 2")
    print(f"🔹 Hallucination Rate: {hallucination_rate:.1f}%")

if __name__ == "__main__":
    evaluate()
