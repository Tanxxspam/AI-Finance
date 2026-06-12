from app.agents.router import route_query

queries = [
    "What is NVDA stock price?",
    "What are NVIDIA risks?",
    "Compare NVIDIA and AMD",
    "Summarize NVIDIA sustainability goals"
]

for q in queries:
    print(q)
    print("→", route_query(q))
    print()