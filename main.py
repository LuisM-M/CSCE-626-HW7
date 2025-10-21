import heapq
# binary min heap implementation

# practice with heapq
he = []
heapq.heappush(he, 1)

print(heapq.heappop(he))


list1 = [5,4,3,2,10, 9, 22]

print(list1)

heapq.heapify(list1)

print(list1)

heapq.heappop(list1)

print(list1)


while list1:
    print(heapq.heappop(list1))



# practice with priority queue

street_dict = {
    'main street': 3,
    'mlk street': 2,
    'bryan avenue': 1,
    'shiraz lane': 4 
}

print("Origianl street distances", street_dict)

pq = [(priority, street) for street, priority in street_dict.items()]

print("Converted to tuples", pq)

heapq.heapify(pq)
print("Converted to heap", pq)

# testing relxation step

# original data structure
d = {'start':0, 'u':2, 'v': 10}
parent = {'u': 'start', 'v': 'start'}


current_node_u = 'u'
neighbor_v = 'v'
weight_u_v = 3 # weight of edge: u to v

print("Original state")
print("Distances (d) ", d)
print("Parents: ", parent)

# relaxtion step

if d[current_node_u] + weight_u_v < d[neighbor_v]:
    print("A better path was found. updating d[v]")

    d[neighbor_v] = d[current_node_u] + weight_u_v
    parent[neighbor_v] = current_node_u

print("end state")
print("Distances (d): ", d)
print("Parents is now:", parent)