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

# Practice -------------
# Prims
def primsMST(graph):

    # Initialize the visited vertices and edges
    visited_vertices = []
    selected_edges = {}

    # Starting points
    start_vertex = list(graph.keys())[0]
    visited_vertices.append(start_vertex)

    # Continue until we visit all vertices
    while len(visited_vertices) < len(graph):
        # We have to find min edge so delcare
        min_edge = None
        min_weight = sys.maxsize

        # Iterate on the current set selected vertices and find their minimum neighbour
        # After getting minimum neighbour, store it and start again from zero, with same steps.
        # Don't stop until visited_vertices becomes equal to graph vertices
        for vertex in visited_vertices:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited_vertices and weight < min_weight:
                    min_edge = (vertex, neighbor)
                    min_weight = weight
        
        # After getting minimum edge, reflect into main answer i.e. selected_edges & visited_vertices
        selected_edges[min_edge] = min_weight
        visited_vertices.append(min_edge[1])
    
    return selected_edges


selected_edges = primsMST(graph)

print("Selected edges:")
for edge, weight in selected_edges.items():
    print(edge, ":", weight)
