from pathlib import Path

from app.rag.retriever import get_retriever
from app.agents.risk_agent import risk_agent

BASE_DIR = Path(__file__).resolve().parents[2]

VECTOR_DIR = BASE_DIR / "vectorstore"

retriever = get_retriever(str(VECTOR_DIR))

query = "What are the major risks faced by the company?"

docs = retriever.invoke(query)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

answer = risk_agent(query, context)

print("\nRISK ANALYSIS\n")
print(answer)