from pathlib import Path

from app.rag.retriever import get_retriever
from app.research_agent import research_agent

BASE_DIR = Path(__file__).resolve().parents[2]

VECTOR_DIR = BASE_DIR / "vectorstore"

retriever = get_retriever(str(VECTOR_DIR))

query = input("Ask a question: ")

docs = retriever.invoke(query)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

answer = research_agent(
    query=query,
    context=context
)

print("\n" + "="*50)
print("ANSWER")
print("="*50)
print(answer)