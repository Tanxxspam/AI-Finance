from app.workflow.graph import graph

result = graph.invoke({
    "query": "What is NVDA stock price?"
})

print(result)