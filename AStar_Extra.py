import heapq

def heuristic(node, goal):
    # Calculate the Manhattan distance between the current node and the goal node
    return abs(ord(node) - ord(goal))

def astar(graph, start, goal):
    # Initialize the open list and add the start node to it
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Initialize dictionaries to store the cost and parent node for each node
    cost = {start: 0}
    parent = {start: None}

    # Iterate until the open list is empty
    while open_list:
        # Pop the node with the lowest cost from the open list
        current_cost, current_node = heapq.heappop(open_list)

        # Check if the current node is the goal node
        if current_node == goal:
            break

        # Explore the neighboring nodes
        for neighbor in graph[current_node]:
            # Calculate the cost from the start node to the neighbor node
            new_cost = cost[current_node] + graph[current_node][neighbor]

            # Check if the neighbor node has not been visited or the new cost is lower
            if neighbor not in cost or new_cost < cost[neighbor]:
                # Update the cost and parent for the neighbor node
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = current_node

    # Reconstruct the path from the goal node to the start node
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    return path


# Example usage
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1}
}

start_node = 'A'
goal_node = 'C'

path = astar(graph, start_node, goal_node)

print("Shortest path from", start_node, "to", goal_node)
print(path)
