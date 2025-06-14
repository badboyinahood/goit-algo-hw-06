import networkx as nx

def build_weighted_graph():
    G = nx.Graph()
    edges = [
        ("Central", "North", 4),
        ("Central", "South", 3),
        ("Central", "East", 5),
        ("Central", "West", 2),
        ("North", "University", 6),
        ("South", "Stadium", 4),
        ("East", "Airport", 7),
        ("West", "Museum", 3),
        ("Museum", "University", 4),
        ("Stadium", "Airport", 2)
    ]
    G.add_weighted_edges_from(edges)
    return G

def dijkstra_all_pairs(graph):
    return dict(nx.all_pairs_dijkstra_path(graph))

if __name__ == "__main__":
    G = build_weighted_graph()
    all_paths = dijkstra_all_pairs(G)

    for source, targets in all_paths.items():
        print(f"\nНайкоротші шляхи з {source}:")
        for target, path in targets.items():
            if source != target:
                print(f"до {target}: {path}")
