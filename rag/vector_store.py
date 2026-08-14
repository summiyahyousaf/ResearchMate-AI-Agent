import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.index=None
        self.chunks=[]


    def add (self, embeddings, chunks):
        vectors=np.array(embeddings).astype("float32")

        if self.index is None:
            dimension=vectors.shape[1]
            self.index=faiss.IndexFlatL2(dimension)

        self.index.add(vectors)
        self.chunks.extend(chunks)


    def search(self, query_embedding, top_k=3):

        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(
            query_vector,
            top_k
        )


        results = []

        for index in indices[0]:
            results.append(self.chunks[index])

        return results