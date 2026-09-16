import os

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore


def get_qdrant_vector_store(embeddings):

    client = QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY")
    )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name="documents",
        embedding=embeddings
    )

    return vector_store


def create_vector_store(chunks, embeddings):

    vector_store = get_qdrant_vector_store(embeddings)

    vector_store.add_documents(chunks)

    return vector_store