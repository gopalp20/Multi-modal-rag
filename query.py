from dotenv import load_dotenv

from processing.embeddings import create_embeddings
from vectorstore.qdrant_store import get_qdrant_vector_store
from retrieval.retriever import retrieve_documents
from llm.chat_model import create_chat_model
from rag.rag_chain import generate_answer


load_dotenv()


# 1. Create embedding model
embeddings = create_embeddings()

print("Embedding model loaded")


# 2. Connect to existing Qdrant collection
vector_store = get_qdrant_vector_store(embeddings)

print("Connected to Qdrant")


# 3. Create chat model
model = create_chat_model()

print("Chat model loaded")


# 4. Take user query
query = input("\nAsk a question about the PDF: ")


# 5. Retrieve relevant chunks
documents = retrieve_documents(
    vector_store,
    query,
    k=3
)

print("Relevant documents retrieved")


# 6. Generate answer
response = generate_answer(
    model,
    documents,
    query
)


# 7. Print answer
print("\n========== ANSWER ==========")
print(response.content)