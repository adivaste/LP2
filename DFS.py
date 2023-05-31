from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
    
    for neighbour in graph[start]-visited:
        dfs(graph, neighbour, visited)


graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'E'}
}

print("DFS traversal : ")
dfs(graph, "A")
 