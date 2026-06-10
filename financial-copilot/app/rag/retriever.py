from app.rag.vector_store import load_vector_store


def get_retriever(vector_db_path):

    vector_store = load_vector_store(vector_db_path)

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return retriever