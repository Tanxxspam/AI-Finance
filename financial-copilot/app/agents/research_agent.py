from app.rag.retriever import get_retriever
from app.agents.research_agent import research_agent

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

def research_agent(query, context):

    prompt = f"""
    You are a Financial Research Analyst.

    Use ONLY the provided context.

    Context:
    {context}

    Question:
    {query}

    Instructions:
    - Give a concise answer
    - Mention key findings
    - Mention supporting evidence
    """

    response = llm.invoke(prompt)

    return response.content