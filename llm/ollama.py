import requests


OLLAMA_URL = "http://localhost:11434/api/chat"


def generate_summary(prompt):

    payload = {
        "model": "llama3.2:1b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "options": {
            "num_predict": 1200
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        return result["message"]["content"]

    except requests.exceptions.RequestException as e:

        print("Ollama Error:", e)

        return "Unable to generate response."