def is_safe(graph, vertex, color, color_assignment):
    # Check if 'color' can be assigned to 'vertex' without conflict
    for neighbor in graph[vertex]:
        if color_assignment[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, vertex, color_assignment):
    if vertex == len(graph):
        # All vertices have been assigned a color
        return True

    for color in colors:
        if is_safe(graph, vertex, color, color_assignment):
            color_assignment[vertex] = color
            if graph_coloring(graph, colors, vertex + 1, color_assignment):
                return True
            color_assignment[vertex] = None

    return False

def solve_graph_coloring(graph, colors):
    num_vertices = len(graph)
    color_assignment = [None] * num_vertices

    if graph_coloring(graph, colors, 0, color_assignment):
        print("Graph can be colored with the following assignments:")
        for vertex, color in enumerate(color_assignment):
            print(f"Vertex {vertex}: Color {color}")
    else:
        print("No valid coloring assignment exists for the graph.")

# Example usage:
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}
colors = ['Red', 'Green', 'Blue']

solve_graph_coloring(graph, colors)


# ----------------------- Practice ------------------------

# Check is Safe or not
def isSafe(graph, vertex, color, color_assignment):
    for neighbor in graph[vertex]:
        if color_assignment[neighbor] == color:
            return False
    return True

# Recursive function for coloring
def graphColoring(graph, vertex, colors, color_assignment):
    if vertex == len(graph):
        return True

    for color in colors:
        if isSafe(graph, vertex, color, color_assignment):
            color_assignment[vertex] = color
            if graphColoring(graph, vertex+1, colors, color_assignment):
                return True
            color_assignment[vertex] = None
    return False
                

# Handle input output for algorithm
def solve(graph, colors):
    color_assignment = [None]*len(graph)

    if graphColoring(graph, 0, colors, color_assignment):
        print("Color assingment is possible with following colors :")
        for vertex,color in enumerate(color_assignment):
            print(vertex, " : ", color)
    else:
        print("No coloring possible for given graph")


# Example/Drivers code
graph = {
    0 : [1, 2, 3],
    1 : [0, 2],
    2 : [0, 1, 3],
    3 : [0, 2]
}
colors = ["Red", "Green", "Blue"]
solve(graph, colors)