def extract_query_info(query: str) -> dict:
    query_lower = query.lower()

    if "compare" in query_lower:
        intent = "supplier_comparison"
    elif "compatible" in query_lower:
        intent = "compatibility_check"
    elif "recommend" in query_lower or "best" in query_lower or "cheap" in query_lower:
        intent = "product_recommendation"
    else:
        intent = "product_search"

    materials = ["insulation", "timber", "steel", "concrete", "adhesive", "coating", "wall panel"]
    properties = ["fire-resistant", "thermal", "waterproof", "durable", "sustainable", "cheap", "low-cost"]

    return {
        "intent": intent,
        "materials": [m for m in materials if m in query_lower],
        "properties": [p for p in properties if p in query_lower],
        "query": query
    }