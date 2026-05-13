import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


class ProductGraph:

    def __init__(self, csv_path="data/products.csv"):

        self.df = pd.read_csv(csv_path)

        self.graph = nx.Graph()

        self.build_graph()

    def build_graph(self):

        for _, row in self.df.iterrows():

            product = row["product_name"]
            material = row["material"]
            supplier = row["supplier"]

            self.graph.add_node(product, type="product")
            self.graph.add_node(material, type="material")
            self.graph.add_node(supplier, type="supplier")

            self.graph.add_edge(
                product,
                material,
                relation="is_a"
            )

            self.graph.add_edge(
                product,
                supplier,
                relation="supplied_by"
            )

            compatible_items = str(
                row["compatible_with"]
            ).split(";")

            for item in compatible_items:

                item = item.strip()

                if item:

                    self.graph.add_node(
                        item,
                        type="compatible_item"
                    )

                    self.graph.add_edge(
                        product,
                        item,
                        relation="compatible_with"
                    )

    def get_relationships(self, product_name):

        if product_name not in self.graph:
            return []

        relationships = []

        for neighbor in self.graph.neighbors(product_name):

            relation = self.graph.edges[
                product_name,
                neighbor
            ]["relation"]

            relationships.append({
                "product": product_name,
                "relation": relation,
                "connected_to": neighbor
            })

        return relationships

    def draw_graph(
        self,
        output_path="graph.png"
    ):

        plt.figure(figsize=(10, 7))

        pos = nx.spring_layout(
            self.graph,
            seed=42
        )

        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_size=2000,
            font_size=8
        )

        edge_labels = nx.get_edge_attributes(
            self.graph,
            "relation"
        )

        nx.draw_networkx_edge_labels(
            self.graph,
            pos,
            edge_labels=edge_labels,
            font_size=7
        )

        plt.tight_layout()

        plt.savefig(
            output_path,
            dpi=200
        )

        plt.close()

        return output_path