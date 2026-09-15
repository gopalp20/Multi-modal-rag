from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


def create_chat_model():

    llm = HuggingFaceEndpoint(
        repo_id="google/gemma-3-27b-it",
        task="text-generation",
        max_new_tokens=512,
        temperature=0.2
    )

    model = ChatHuggingFace(
        llm=llm
    )

    return model