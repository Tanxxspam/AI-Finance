from pathlib import Path

from pdf_loader import load_pdfs
from chunker import chunk_documents
from vector_store import create_vector_store, save_vector_store


BASE_DIR = Path(__file__).resolve().parents[2]

REPORTS_DIR = BASE_DIR / "data" / "reports"
VECTOR_DIR = BASE_DIR / "vectorstore"

docs = load_pdfs(str(REPORTS_DIR))

chunks = chunk_documents(docs)

print(f"Chunks: {len(chunks)}")

vector_store = create_vector_store(chunks)

save_vector_store(vector_store, str(VECTOR_DIR))

print("\nFAISS index created successfully!")