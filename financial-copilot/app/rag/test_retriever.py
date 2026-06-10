from pathlib import Path

from retriever import get_retriever

BASE_DIR = Path(__file__).resolve().parents[2]

VECTOR_DIR = BASE_DIR / "vectorstore"

retriever = get_retriever(str(VECTOR_DIR))

query = "What are NVIDIA's sustainability goals?"

results = retriever.invoke(query)

print(f"\nRetrieved {len(results)} chunks\n")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print(doc.page_content[:500])