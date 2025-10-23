import heapq

# map renamed to G to match pseudocode
G = {
    's': {'t': 10, 'y': 5},
    't': {'x': 1, 'y': 2},
    'x': {'z': 4},
    'y': {'t': 3, 'x': 9, 'z': 2},
    'z': {'s': 7, 'x': 6}
}
s = 's'

def dijkstra(graph, source_node):
# intialization
    d = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    d[source_node] = 0
    parent[source_node] = source_node

    
    # Enqueue the source node
    Q = [(0, source_node)]


    print("Distances: ", d)
    print("Parents: ", parent)
    print("Priority Queue: ", Q)

    print()
    return d, parent

print("Testing initialization")
dijkstra(G,s)


