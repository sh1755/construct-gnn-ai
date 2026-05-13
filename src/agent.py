from src.nlp import extract_query_info


class ConstructionAgent:
    def __init__(self, rag, graph):
        self.rag = rag
        self.graph = graph

    def run(self, query: str):
        info = extract_query_info(query)
        intent = info["intent"]

        if intent == "supplier_comparison":
            return self.compare_suppliers(query, info)
        elif intent == "compatibility_check":
            return self.check_compatibility(query, info)
        elif intent == "product_recommendation":
            return self.recommend_product(query, info)
        else:
            return self.search_product(query, info)

    def search_product(self, query, info):
        results = self.rag.search(query)
        return {
            "intent": info,
            "agent_decision": "Product search using semantic retrieval",
            "results": results
        }

    def recommend_product(self, query, info):
        results = self.rag.search(query)
        sorted_results = sorted(results, key=lambda x: float(x["price"]))

        return {
            "intent": info,
            "agent_decision": "Recommendation using RAG retrieval + price ranking",
            "results": sorted_results
        }

    def check_compatibility(self, query, info):
        results = self.rag.search(query)

        graph_relations = {}
        for item in results:
            product = item["product_name"]
            graph_relations[product] = self.graph.get_relationships(product)

        return {
            "intent": info,
            "agent_decision": "Compatibility analysis using graph relationships",
            "results": results,
            "graph_relationships": graph_relations
        }

    def compare_suppliers(self, query, info):
        results = self.rag.search(query)

        suppliers = {}
        for item in results:
            supplier = item["supplier"]
            suppliers.setdefault(supplier, []).append(item)

        return {
            "intent": info,
            "agent_decision": "Supplier comparison using retrieved product data",
            "results": suppliers
        }