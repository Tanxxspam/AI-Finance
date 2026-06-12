from app.agents.market_agent import market_agent

def market_node(state):

    query = state["query"]

    if "nvda" in query.lower():
        ticker = "NVDA"
    elif "aapl" in query.lower():
        ticker = "AAPL"
    else:
        ticker = "NVDA"

    state["response"] = market_agent(query, ticker)

    return state