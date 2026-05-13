import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


class ProductRAG:
    def __init__(self, csv_path="data/products.csv"):
        self.df = pd.read_csv(csv_path)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.texts = self.df.apply(
            lambda row: f"{row['product_name']} {row['material']} {row['properties']} "
                        f"{row['compatible_with']} {row['supplier']} price {row['price']}",
            axis=1
        ).tolist()

        embeddings = self.model.encode(self.texts)
        self.embeddings = np.array(embeddings).astype("float32")

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def search(self, query: str, top_k: int = 3):
        q_emb = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(q_emb, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.df.iloc[idx].to_dict())

        return results