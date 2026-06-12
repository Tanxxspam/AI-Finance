def route_query(query):

    query = query.lower()

    if any(word in query for word in [
        "price",
        "market cap",
        "stock",
        "pe ratio"
    ]):
        return "market"

    elif any(word in query for word in [
        "risk",
        "threat",
        "challenge",
        "uncertainty"
    ]):
        return "risk"

    elif "compare" in query:
        return "comparison"

    return "research"