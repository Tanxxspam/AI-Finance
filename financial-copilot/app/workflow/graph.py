from langgraph.graph import StateGraph, END

from app.workflow.state import AgentState

from app.workflow.router_node import router_node
from app.workflow.research_node import research_node
from app.workflow.market_node import market_node
from app.workflow.risk_node import risk_node
from app.workflow.comparison_node import comparison_node

workflow = StateGraph(AgentState)

# Nodes
workflow.add_node("router", router_node)
workflow.add_node("research", research_node)
workflow.add_node("market", market_node)
workflow.add_node("risk", risk_node)
workflow.add_node("comparison", comparison_node)

# Entry Point
workflow.set_entry_point("router")

# ADD CONDITIONAL ROUTING HERE
workflow.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "research": "research",
        "market": "market",
        "risk": "risk",
        "comparison": "comparison",
    }
)

# End Connections
workflow.add_edge("research", END)
workflow.add_edge("market", END)
workflow.add_edge("risk", END)
workflow.add_edge("comparison", END)

graph = workflow.compile()