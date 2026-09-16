from langchain_core.prompts import PromptTemplate


def create_rag_prompt():

    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.

        Answer the question using only the provided context.

        If the answer is not present in the context, say:
        "I don't know based on the provided document."

        Do not make up information.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """,
        input_variables=["context", "question"]
    )

    return prompt