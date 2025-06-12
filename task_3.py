def print_table(distances, visited):
    # Column names
    print("{:<25} {:<15} {:<15}".format("City", "Distance", "Visited"))
    print("-" * 40)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "No"
        print("{:<25} {:<15} {:<10}".format(vertex, distance, status))
    print("\\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        print_table(distances, visited)

    return distances

# Приклад графа у вигляді словника
cities_graph = {
    "Kyiv": {"Zhytomyr": 140, "Vinnytsia": 265},
    "Zhytomyr": {"Kyiv": 140, "Khmelnytskyi": 195, "Rivne": 190},
    "Vinnytsia": {"Kyiv": 265, "Khmelnytskyi": 120},
    "Khmelnytskyi": {"Zhytomyr": 195, "Vinnytsia": 120, "Ternopil": 110},
    "Rivne": {"Zhytomyr": 190, "Lutsk": 75, "Ternopil": 160},
    "Lutsk": {"Rivne": 75, "Lviv": 170},
    "Ternopil": {"Rivne": 160, "Lviv": 130, "Ivano-Frankivsk": 130, "Khmelnytskyi": 110},
    "Ivano-Frankivsk": {"Ternopil": 130, "Lviv": 140},
    "Lviv": {"Ternopil": 130, "Lutsk": 170, "Ivano-Frankivsk": 140}
}

# Виклик функції для вершини A
dijkstra(cities_graph, 'Kyiv')
