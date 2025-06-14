import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

stations = ["Central", "North", "South", "East", "West", "Museum", "Stadium", "Airport", "University"]
G.add_nodes_from(stations)

edges = [
    ("Central", "North"),
    ("Central", "South"),
    ("Central", "East"),
    ("Central", "West"),
    ("North", "University"),
    ("South", "Stadium"),
    ("East", "Airport"),
    ("West", "Museum"),
    ("Museum", "University"),
    ("Stadium", "Airport")
]

G.add_edges_from(edges)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=12)
plt.title("Транспортна мережа міста")
plt.show()

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("\nСтупені вершин:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
