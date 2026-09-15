from ingestion.pdf_loader import load_pdf
from processing.text_splitter import split_documents
from processing.embeddings import create_embeddings

from dotenv import load_dotenv


load_dotenv()

pdf_path = "data/sample.pdf"

documents = load_pdf(pdf_path)

print("Documents:", len(documents))

chunks = split_documents(documents)

print("Chunks:", len(chunks))

embeddings = create_embeddings()

vector = embeddings.embed_query(
    "What programming languages are mentioned?"
)

print("\nEmbedding dimensions:")
print(len(vector))

print("\nFirst 5 values:")
print(vector[:5])