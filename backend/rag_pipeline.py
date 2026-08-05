from backend.pdf_loader import load_pdf
from backend.chunker import create_chunks
from backend.embeddings import get_embedding_model
from backend.vector_store import create_vector_store
from backend.llm.llm_service import LLMService

db = None
llm = LLMService()

def build_index(pdf_path):
    global db

    documents = load_pdf(pdf_path)
    chunks = create_chunks(documents)
    embedding_model = get_embedding_model()

    db = create_vector_store(
        chunks=chunks,
        embedding_model=embedding_model
    )

def ask_question(question):
    

    if db is None:
        return "Please upload a PDF first 📄"

    chunks = db.similarity_search(question, k=4)
    print("\n========== RETRIEVED CHUNKS ==========\n")

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}")
        print(f"Page: {chunk.metadata.get('page')}")
        print(chunk.page_content)
        print("-" * 80)
    context = "\n\n".join(
        f"[page {chunk.metadata['page'] + 1}] {chunk.page_content}"
        for chunk in chunks
    )

    return llm.invoke(
        context=context,
        question=question
    )