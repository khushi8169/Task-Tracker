from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

INDEX_PATH = "faiss_index"

if os.path.exists(f"{INDEX_PATH}/index.faiss"):
    db = FAISS.load_local(INDEX_PATH, embedding, allow_dangerous_deserialization=True)
else:
    # Initialize with at least one dummy text to avoid empty list error
    db = FAISS.from_texts(["initial placeholder task"], embedding)
    db.save_local(INDEX_PATH)

def add_to_vector_store(text: str):
    db.add_texts([text])
    db.save_local(INDEX_PATH)

def search_similar(query: str):
    return db.similarity_search(query, k=3)
