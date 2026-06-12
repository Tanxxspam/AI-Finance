from fastapi import APIRouter
from app.workflow.graph import graph

router = APIRouter()

@router.post("/query")
def query_agent(data: dict):
    result = graph.invoke({
        "query": data["query"]
    })

    return result 