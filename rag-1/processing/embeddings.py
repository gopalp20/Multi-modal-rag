from langchain_huggingface import HuggingFaceEndpointEmbeddings
import os


def create_embeddings():

    embeddings = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        task="feature-extraction",
        huggingfacehub_api_token=os.getenv("HF_TOKEN")
    )

    return embeddings