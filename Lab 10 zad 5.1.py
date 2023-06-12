import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v

        return min_index

    def prim(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V
        key[0] = 0

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        result = []
        for i in range(1, self.V):
            result.append([parent[i], i, self.graph[i][parent[i]]])

        return result


# Przykład użycia:
g = Graph(4)
g.graph = [[0, 10, 6, 5],
           [10, 0, 0, 15],
           [6, 0, 0, 4],
           [5, 15, 4, 0]]

print("MST (Prims):")
mst = g.prim()
for u, v, weight in mst:
    print(f"{u} -- {v}  {weight}")