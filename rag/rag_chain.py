from llm.prompts import create_rag_prompt


def generate_answer(model, documents, query):

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = create_rag_prompt()

    final_prompt = prompt.format(
        context=context,
        question=query
    )

    response = model.invoke(final_prompt)

    return response