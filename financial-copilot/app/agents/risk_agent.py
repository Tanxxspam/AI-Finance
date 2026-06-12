from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

def risk_agent(query, context):

    prompt = f"""
    You are a Financial Risk Analyst.

    Use ONLY the provided context.

    Context:
    {context}

    Question:
    {query}

    Extract:

    1. Financial Risks
    2. Operational Risks
    3. Market Risks
    4. Regulatory Risks
    5. Overall Risk Summary

    Be concise and evidence-based.
    """

    response = llm.invoke(prompt)

    return response.content