from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are an expert in global affairs.

Using ONLY the information below, answer the question.

Rules:
- Do not repeat the question
- Do not add information not present in the context
- Write 4 to 6 sentences
- Be clear, neutral, and factual

Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(
        prompt,
        max_length=500,
        do_sample=False
    )

    return result[0]["generated_text"].strip()