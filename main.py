from dotenv import load_dotenv

from ingestion.pdf_loader import load_pdf
from processing.text_splitter import split_documents
from processing.embeddings import create_embeddings

from vectorstore.qdrant_store import create_vector_store

from retrieval.retriever import retrieve_documents

from llm.chat_model import create_chat_model

from rag.rag_chain import generate_answer


load_dotenv()


# -----------------------------
# 1. Load PDF
# -----------------------------

pdf_path = "data/sample.pdf"

documents = load_pdf(pdf_path)

print("Documents:", len(documents))


# -----------------------------
# 2. Split into chunks
# -----------------------------

chunks = split_documents(documents)

print("Chunks:", len(chunks))


# -----------------------------
# 3. Create embedding model
# -----------------------------

embeddings = create_embeddings()

print("Embedding model loaded")


# -----------------------------
# 4. Store chunks in Chroma
# -----------------------------

vector_store = create_vector_store(
    chunks,
    embeddings
)
print("Chunks stored in Qdrant Cloud")


# -----------------------------
# 5. Create chat model
# -----------------------------

model = create_chat_model()

print("Chat model loaded")


# -----------------------------
# 6. Take user query
# -----------------------------

query = input("\nAsk a question about the PDF: ")


# -----------------------------
# 7. Retrieve relevant chunks
# -----------------------------

documents = retrieve_documents(
    vector_store,
    query,
    k=3
)


# print("\nRetrieved documents:")

# for i, document in enumerate(documents):

#     print(f"\n--- Document {i + 1} ---")

#     print(document.page_content)

#     print("\nMetadata:")
#     print(document.metadata)


# -----------------------------
# 8. Generate answer
# -----------------------------

response = generate_answer(
    model,
    documents,
    query
)


# -----------------------------
# 9. Print response
# -----------------------------

print("\n========== ANSWER ==========")

print(response.content)