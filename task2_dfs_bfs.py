import networkx as nx
from collections import deque

def build_graph():
    G = nx.Graph()
    stations = ["Central", "North", "South", "East", "West", "Museum", "Stadium", "Airport", "University"]
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
    G.add_nodes_from(stations)
    G.add_edges_from(edges)
    return G

def dfs_path(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    return None

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

if __name__ == "__main__":
    G = build_graph()
    start, goal = "University", "Airport"

    dfs = dfs_path(G, start, goal)
    bfs = bfs_path(G, start, goal)

    print("DFS path:", dfs)
    print("BFS path:", bfs)
