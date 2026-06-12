from app.rag.retriever import get_retriever
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
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

USE_MOCK = True

def research_agent(query, context):

    if USE_MOCK:
        return f"Mock answer for: {query}"

    prompt = f"""
    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    return response.content