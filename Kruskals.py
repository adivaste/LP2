class UnionFind:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}

        for vertex in vertices:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def kruskal(graph):
    # Create a list to store the selected edges and their weights
    selected_edges = []

    # Get all the edges from the graph
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((vertex, neighbor, weight))

    # Sort the edges in non-decreasing order of weight
    edges.sort(key=lambda x: x[2])

    # Create a UnionFind data structure with the vertices of the graph
    vertices = list(graph.keys())
    uf = UnionFind(vertices)

    # Iterate over the sorted edges and add them to the MST if they do not create a cycle
    for edge in edges:
        vertex1, vertex2, weight = edge
        if uf.find(vertex1) != uf.find(vertex2):
            uf.union(vertex1, vertex2)
            selected_edges.append(edge)

    return selected_edges


# Example usage
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1}
}

selected_edges = kruskal(graph)

print("Selected edges:")
for edge in selected_edges:
    print(edge[0], "--", edge[1], ":", edge[2])
