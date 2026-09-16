def retrieve_documents(vector_store, query, k=3):

    documents = vector_store.similarity_search(
        query,
        k=k
    )

    return documents