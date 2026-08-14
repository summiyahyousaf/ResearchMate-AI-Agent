import os
from dotenv import load_dotenv
#Python client that can communicate with Hugging Face's hosted models.
from huggingface_hub import InferenceClient

load_dotenv()

API_KEY=os.getenv("HUGGINGFACE_API_KEY")

client=InferenceClient(token=API_KEY)

def create_embedding(text):
    embedding=client.feature_extraction(text,model="sentence-transformers/all-MiniLM-L6-v2")

    return embedding
