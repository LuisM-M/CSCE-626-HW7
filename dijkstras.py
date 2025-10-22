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

print()
print("first iteration ############")

# u:= extract-min(Q)

current_dist, u = heapq.heappop(Q)

print("Popped", u, "with distance", current_dist,"from S")
print("Q after pop:", Q)

print("Relaxing neighbors of S")
for v, weight in map[u].items():
    if d[u] + weight < d[v]:
        print("\tUpdating", v, "with distance:", d[v])
        print("\twith NEW distance of:" , d[u] + weight)
        print()
        d[v] = d[u] + weight
        parent[v] = u
        heapq.heappush(Q, (d[v], v))


print("Distances: ", d)
print("Parents: ", parent)
print("Priority Queue: ", Q)
print()

# popping A and relaxation of neighbors

print("Popping A and proper steps ############")
current_dist, u = heapq.heappop(Q)

print("Popped", u, "with distance", current_dist,"from S")
print("Q after pop:", Q)

print("Relaxing neighbors of A")
for v, weight in map[u].items():
    if v ==s:
        continue
    if d[u] + weight < d[v]:
        print("\tUpdating", v, "with distance:", d[v])
        print("\twith NEW distance of:" , d[u] + weight)
        print()
        d[v] = d[u] + weight
        parent[v] = u
        heapq.heappush(Q, (d[v], v))
    else:
        print("No update for", v, "path through A is not better than current")


print("Distances: ", d)
print("Parents: ", parent)
print("Priority Queue: ", Q)
print()


