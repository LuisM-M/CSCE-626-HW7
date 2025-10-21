import heapq


map = {
    'S': {'A': 1, 'C': 5 },
    'A': {'S': 1, 'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1},
    'C': {'S': 5, 'A': 3, 'B': 1}
}
s = 'S'

# intialization
d = {node: float('inf') for node in map}
d[s] = 0

parent = {node: None for node in map}

Q = [(0, s)]


print("Distances: ", d)
print("Parents: ", parent)
print("Priority Queue: ", Q)

