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





---

# Project Structure

```text
construct-gnn-ai/
│
├── data/
│   └── construction_products.csv
│
├── src/
│   ├── __init__.py
│   ├── graph.py
│   ├── gnn_model.py
│   ├── train.py
│   ├── predict.py
│   ├── nlp.py
│   ├── rag.py
│   ├── agent.py
│   └── utils.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── models/
    └── saved_model.pt
```

---

# Overview

Construct-GNN-AI is an intelligent AI platform for the construction industry that combines:

- Graph Neural Networks (GNN)
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG)
- AI Agents

The system analyses relationships between construction materials, suppliers, technical specifications, and product compatibility to generate intelligent recommendations and insights.

---

# Features

- Supplier recommendation system
- Material compatibility analysis
- Product relationship graph analysis
- Semantic search using embeddings
- AI-powered technical question answering
- RAG-based document retrieval
- Multi-agent reasoning workflow
- Streamlit interactive dashboard

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PyTorch | Deep learning framework |
| PyTorch Geometric | Graph Neural Networks |
| NetworkX | Graph construction |
| LangChain | RAG pipeline |
| FAISS | Vector database |
| Sentence Transformers | Embeddings |
| Transformers | NLP models |
| Streamlit | Web application |
| Pandas | Data processing |

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/construct-gnn-ai.git
cd construct-gnn-ai
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```text
torch
torch-geometric
pandas
numpy
scikit-learn
networkx
matplotlib
streamlit
sentence-transformers
transformers
langchain
faiss-cpu
```

---

# System Workflow

```text
Construction Product Data
            ↓
NLP Text Processing
            ↓
Embedding Generation
            ↓
Graph Creation using NetworkX
            ↓
GNN Model Training
            ↓
Relationship Learning
            ↓
Supplier & Material Recommendation
            ↓
RAG Retrieval System
            ↓
AI Agent Reasoning
            ↓
Streamlit Dashboard Output
```

---

# Example Use Cases

## Supplier Recommendation

Find the best supplier based on:

- Product similarity
- Pricing
- Material quality
- Delivery performance

---

## Material Compatibility

Analyse whether two construction materials can work together safely and efficiently.

---

## Product Relationship Analysis

Use GNN to discover hidden relationships between:

- Materials
- Suppliers
- Product categories
- Technical specifications

---

# Run the Project

```bash
streamlit run app.py
```

---

# Future Improvements

- Multi-agent collaboration
- Cloud deployment using Docker & Kubernetes
- Real-time construction data ingestion
- Knowledge graph expansion
- LLM-based report generation

---

# Author

Sajjad Hussain
Researcher in AI  
University of Brighton  
United Kingdom

