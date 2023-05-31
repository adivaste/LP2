import sys

def prim(graph):
    # Initialize a list to store the selected vertices
    selected = []
    # Initialize a dictionary to store the selected edges and their weights
    selected_edges = {}

    # Select the first vertex as the starting point
    start_vertex = list(graph.keys())[0]
    selected.append(start_vertex)

    # Repeat until all vertices are selected
    while len(selected) < len(graph):
        min_weight = sys.maxsize
        min_edge = None

        # Iterate over the selected vertices and find the minimum weight edge connecting to an unselected vertex
        for vertex in selected:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in selected and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)

        # Add the minimum weight edge to the selected edges
        selected_edges[min_edge] = min_weight

        # Add the newly selected vertex to the selected list
        selected.append(min_edge[1])

    return selected_edges


# Example usage
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1}
}

selected_edges = prim(graph)

print("Selected edges:")
for edge, weight in selected_edges.items():
    print(edge, ":", weight)
