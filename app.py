import streamlit as st

from src.rag import ProductRAG
from src.graph import ProductGraph
from src.agent import ConstructionAgent


st.set_page_config(
    page_title="Construct GNN AI",
    layout="wide"
)

st.title("Construct GNN AI")
st.write("NLP + RAG + Graph Relationship Intelligence for construction product recommendation")

@st.cache_resource
def load_system():
    rag = ProductRAG()
    graph = ProductGraph()
    agent = ConstructionAgent(rag, graph)
    return rag, graph, agent

rag, graph, agent = load_system()

query = st.text_input(
    "Ask a construction product question:",
    "Find cheap fire-resistant insulation compatible with timber walls"
)

if st.button("Run AI Agent"):
    response = agent.run(query)

    st.subheader("Agent Decision")
    st.write(response["agent_decision"])

    st.subheader("NLP Output")
    st.json(response["intent"])

    st.subheader("Results")
    st.json(response["results"])

    if "graph_relationships" in response:
        st.subheader("Graph Relationships")
        st.json(response["graph_relationships"])

st.divider()

if st.button("Show Product Graph"):
    graph_path = graph.draw_graph("construction_product_graph.png")
    st.image(graph_path, caption="Construction Product Relationship Graph")