from dotenv import load_dotenv
load_dotenv()
from ingestion.pdf_loader import load_pdf
from processing.text_splitter import split_documents
from processing.embeddings import create_embeddings
from vectorstore.qdrant_store import create_vector_store


def ingest_pdf(file_path):

    # 1. Load PDF
    documents = load_pdf(file_path)

    print("Documents:", len(documents))

    # 2. Split into chunks
    chunks = split_documents(documents)

    print("Chunks:", len(chunks))

    # 3. Create embeddings
    embeddings = create_embeddings()

    print("Embedding model loaded")

    # 4. Store chunks in Qdrant
    create_vector_store(
        chunks,
        embeddings
    )

    print("Chunks stored in Qdrant")