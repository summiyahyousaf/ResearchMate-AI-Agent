from llm.huggingface import generate_summary


prompt = """
Explain what Generative AI is in simple terms.

Give me:
1. Definition
2. How it works
3. Three applications
4. One limitation
"""


response = generate_summary(prompt)

print("\n========== LLM RESPONSE ==========\n")
print(response)