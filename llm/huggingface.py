import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_summary(prompt):

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1000,
        "temperature": 0.3
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    print("\n========== HUGGING FACE ==========")
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)
    print("==================================\n")

    response.raise_for_status()

    result = response.json()

    return result["choices"][0]["message"]["content"]
