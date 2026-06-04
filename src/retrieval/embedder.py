from sentence_transformers import SentenceTransformer
def chunk_text(text, chunk_size=600, overlap=100):
    """
    Split text into overlapping chunks for embedding.
    """
    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

# Load the model offline
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
def embed_texts(texts):
    return model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
