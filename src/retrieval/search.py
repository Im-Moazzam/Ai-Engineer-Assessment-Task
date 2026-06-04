from .embedder import chunk_text, embed_texts, model
from .vector_store import VectorStore


def build_index(documents):
    """
    documents: list of dicts with keys: filename, text, class
    """
    all_chunks = []
    meta_list = []

    for doc in documents:
        chunks = chunk_text(doc["text"])
        for chunk in chunks:
            all_chunks.append(chunk)
            meta_list.append(
                {"filename": doc["filename"], "class": doc["class"], "text": chunk})

    embeddings = embed_texts(all_chunks)
    dim = embeddings.shape[1]
    store = VectorStore(dim)
    store.add(embeddings, meta_list)
    return store


def query_index(store, query, top_k=5):
    query_emb = model.encode(
        [query], convert_to_numpy=True, normalize_embeddings=True)[0]
    return store.search(query_emb, top_k)
