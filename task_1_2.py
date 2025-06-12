import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()

# Graph for the route fromKyiv to Lviv
    cities = [
        "Kyiv",
        "Zhytomyr",
        "Rivne",
        "Lutsk",
        "Lviv",
        "Vinnytsia",
        "Khmelnytskyi",
        "Ternopil",
        "Ivano-Frankivsk"
    ]
    G.add_nodes_from(cities)

    routes = [
        ("Kyiv", "Zhytomyr", 140),
        ("Kyiv", "Vinnytsia", 265),
        ("Zhytomyr", "Khmelnytskyi", 195),
        ("Zhytomyr", "Rivne", 190),
        ("Vinnytsia", "Khmelnytskyi", 120),
        ("Rivne", "Lutsk", 75),
        ("Rivne", "Ternopil", 160),
        ("Ternopil", "Lviv", 130),
        ("Lutsk", "Lviv", 170),
        ("Ternopil", "Ivano-Frankivsk", 130),
        ("Khmelnytskyi", "Ternopil", 110),
        ("Ivano-Frankivsk", "Lviv", 140)
    ]
    G.add_weighted_edges_from(routes)

    return G

# For 2nd task for choosing the route
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path=[start]
    if visited is None:
        visited = set()
    visited.add(start)

    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if result is not None:
                return result
    return None

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    visited= set()

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None



if __name__ == "__main__":
    G = create_graph()

# Statistic for the graph
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"Кількість міст: {num_nodes}")
print(f"Кількість з'єднань: {num_edges}")


# Vertex colors
node_colors = []

for node in G.nodes():
    if node == "Kyiv":
        node_colors.append("red")
    elif node == "Lviv":
        node_colors.append("green")
    else:
        node_colors.append("grey")

# Vertex position
pos = {
    "Kyiv": (10, 5),
    "Zhytomyr": (8.5, 5),
    "Vinnytsia": (7.5, 3.5),
    "Khmelnytskyi": (6, 4),
    "Rivne": (7.5, 6.5),
    "Lutsk": (6.5, 7.5),
    "Ternopil": (5, 5),
    "Ivano-Frankivsk": (4, 4),
    "Lviv": (3, 6)
}


# Drawing the graph
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors, font_size=10, font_weight='bold', edge_color='lightgrey')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d} км" for u, v, d in G.edges(data='weight')})
plt.title("From Kyiv to Lviv")
plt.show()


# Choosing the route via DFS(Depth-first search) and BFS(Breadth-first search)
start = "Kyiv"
goal = "Lviv"

path_dfs = dfs_path(G, start, goal)
path_bfs = bfs_path(G, start, goal)


print(f"DFS шлях з {start} до {goal}: {path_dfs}")
print(f"BFS шлях з {start} до {goal}: {path_bfs}")