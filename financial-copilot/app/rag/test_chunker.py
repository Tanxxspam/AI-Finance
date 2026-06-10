from pathlib import Path

from pdf_loader import load_pdfs
from chunker import chunk_documents


BASE_DIR = Path(__file__).resolve().parents[2]

REPORTS_DIR = BASE_DIR / "data" / "reports"

docs = load_pdfs(str(REPORTS_DIR))

print(f"Pages Loaded: {len(docs)}")

chunks = chunk_documents(docs)

print(f"Chunks Created: {len(chunks)}")

print("\nSample Chunk:\n")
print(chunks[0].page_content[:500])

print("\nMetadata:\n")
print(chunks[0].metadata)