import sys

def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize empty set for visited nodes
    visited = set()

    # Iterate through all nodes in the graph
    while len(visited) < len(graph):
        # Find the node with the minimum distance that has not been visited
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # Mark the minimum distance node as visited
        visited.add(min_node)

        # Update the distances of the neighboring nodes
        for neighbor, weight in graph[min_node].items():
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


# Example usage
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print("To node", node + ":", distance)