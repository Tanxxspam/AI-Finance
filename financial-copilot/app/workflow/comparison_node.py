from app.agents.comparison_agent import comparison_agent

def comparison_node(state):

    state["response"] = comparison_agent(
        "NVDA",
        "AMD"
    )

    return state