from rag.embeddings import create_embedding
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.store = VectorStore()

    def add_documents(self, chunks):
        embeddings = []

        for chunk in chunks:
            embedding = create_embedding(chunk)
            embeddings.append(embedding)

        self.store.add(embeddings, chunks)

    def retrieve(self, query, top_k=3):
        query_embedding = create_embedding(query)

        results = self.store.search(
            query_embedding,
            top_k
        )

        return results