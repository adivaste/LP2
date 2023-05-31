# Importing the required data structures
from collections import deque


# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, " ", end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)


# Driver's code
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("BFS traversal : ", end=" ")
bfs(graph, "A")
