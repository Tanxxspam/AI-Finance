from app.agents.risk_agent import risk_agent

def risk_node(state):

    query = state["query"]

    state["response"] = f"Risk analysis for: {query}"

    return state