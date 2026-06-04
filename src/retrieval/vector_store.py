import faiss
import numpy as np


class VectorStore:
    def __init__(self, dim):
        # Use cosine similarity
        self.index = faiss.IndexFlatIP(dim)
        self.metadata = []

    def add(self, embeddings, meta_list):
        self.index.add(embeddings)
        self.metadata.extend(meta_list)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding]), top_k)
        results = []
        for score, idx in zip(D[0], I[0]):
            results.append({
                "score": float(score),
                "text": self.metadata[idx]["text"],
                "filename": self.metadata[idx]["filename"],
                "class": self.metadata[idx]["class"]
            })
        return results
