import heapq

# Klasa reprezentująca graf
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    # Dodawanie wierzchołka do grafu
    def add_node(self, node):
        self.nodes.add(node)
        self.edges[node] = {}

    # Dodawanie krawędzi do grafu
    def add_edge(self, start, end, weight):
        self.edges[start][end] = weight
        self.edges[end][start] = weight

    # Wyznaczanie najkrótszej drogi w grafie
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        queue = [(0, start)]
        visited = set()

        while queue:
            current_distance, current_node = heapq.heappop(queue)
            visited.add(current_node)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

# Tworzenie grafu
graph = Graph()

# Dodawanie wierzchołków
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

# Dodawanie krawędzi
graph.add_edge("A", "B", 6)
graph.add_edge("A", "D", 1)
graph.add_edge("B", "C", 5)
graph.add_edge("B", "D", 2)
graph.add_edge("B", "E", 2)
graph.add_edge("C", "E", 5)
graph.add_edge("D", "E", 1)

# Wyznaczanie najkrótszej drogi z wierzchołka A
distances = graph.dijkstra("A")

# Wyświetlanie wyników
for node, distance in distances.items():
    print(f"Najkrótsza droga z wierzchołka A do {node}: {distance}")

#WYNIKI
# Najkrótsza droga z wierzchołka A do A: 0
# Najkrótsza droga z wierzchołka A do B: 3
# Najkrótsza droga z wierzchołka A do C: 8
# Najkrótsza droga z wierzchołka A do D: 1
# Najkrótsza droga z wierzchołka A do E: 2
