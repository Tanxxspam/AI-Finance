from app.agents.router import route_query

def router_node(state):
    state["route"] = route_query(state["query"])
    return state