# ConstructGNN-AI

AI-powered Construction Intelligence System using NLP, Graph Neural Networks, RAG, and LLMs for construction product search, supplier recommendation, material compatibility analysis, and product relationship reasoning.

---

## Overview

ConstructGNN-AI is a mini AI project designed for the construction industry. It helps users search construction products, compare suppliers, analyse material compatibility, and generate intelligent recommendations.

The system combines:

- NLP to understand construction text
- GNN to learn relationships between products, suppliers, and materials
- RAG to retrieve accurate information from documents
- LLM to generate final answers
- Streamlit to provide a simple web interface

---

## Main Features

- Construction product search
- Supplier recommendation
- Material compatibility analysis
- Product relationship analysis
- Knowledge graph creation
- RAG-based question answering
- LLM-powered recommendation generation
- Streamlit web application

---

## System Flowchart

```text
User Query
    |
    v
Streamlit Web Interface
    |
    v
NLP Processing
    |
    v
Intent Detection
    |
    +-----------------------------+
    |                             |
    v                             v
RAG Pipeline                  Knowledge Graph
PDF / CSV Data                Product-Supplier-Material Graph
    |                             |
    v                             v
Text Chunking                 Graph Construction
    |                             |
    v                             v
Embedding Model               GNN Model
    |                             |
    v                             v
FAISS Vector Database         Relationship Learning
    |                             |
    +-------------+---------------+
                  |
                  v
          Recommendation Engine
                  |
                  v
              LLM / Ollama
                  |
                  v
          Final AI Response


          +--------------------------------------------------+
|                  User Interface                  |
|                 Streamlit Web App                |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|                  NLP Layer                       |
|  Text Cleaning | Tokenization | Intent Detection |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|                Data Processing Layer             |
|       CSV Data | PDF Catalogues | Supplier Data   |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------+-----------------------+
|                                                  |
|              AI Intelligence Layer               |
|                                                  |
|  +----------------------+    +----------------+  |
|  | RAG Pipeline         |    | GNN Pipeline   |  |
|  | Chunking             |    | Knowledge Graph|  |
|  | Embeddings           |    | Node Features  |  |
|  | FAISS Search         |    | Edge Relations |  |
|  +----------------------+    +----------------+  |
|                                                  |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|              Recommendation Engine               |
| Supplier Ranking | Compatibility | Product Match |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|                 LLM Response Layer               |
|              Ollama / Llama / Mistral            |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|                  Final Answer                    |
|       Recommendation with Explanation            |
+--------------------------------------------------+
