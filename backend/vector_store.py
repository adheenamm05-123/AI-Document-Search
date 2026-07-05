from langchain_community.vectorstores import FAISS
from embeddings import embedding_model


def create_vector_store(chunks):
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )
    return vector_store


def search_chunks(vector_store, query):
    return vector_store.similarity_search(query, k=3)