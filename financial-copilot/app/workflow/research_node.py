from app.rag.retriever import get_retriever
from app.agents.research_agent import research_agent

def research_node(state):

    retriever = get_retriever("vectorstore")

    docs = retriever.invoke(state["query"])

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    answer = research_agent(
        state["query"],
        context
    )

    state["response"] = answer

    return state