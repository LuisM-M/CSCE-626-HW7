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
    iteration = 0
    while Q:
        iteration = iteration + 1
        print("_______ ITERATION ", iteration,"________" )

        # u:= extract-min(Q)
        current_distance, u = heapq.heappop(Q)
        print("Popped node ", u, "with distance", current_distance )
        

        # check to see if we already found a shorter path to u
        # Necessary to make changes to the heap. its an alternative to decrease-key
        if current_distance > d[u]:
            # print("Distance", current_distance, )
            continue

        # for each neighbor v of u { 
        print("  Checking neighbors of '", u, "':")
        for v, weight in graph[u].items():
            print("    > Neighbor: '", v, "', Edge w(u,v): ", weight, sep='')

            # if (d[u] + w(u,v) < d[v]) { // relax
            if d[u] + weight < d[v]:
                print("      Relaxing edge (", u, ",", v, "): Path through '", u, "' (", d[u] + weight, ") is < current d['", v, "'] (", d[v], ")")

                # d[v] := d[u] + w(u,v);
                d[v] = d[u] + weight

                # parent(v) := u;
                parent[v] = u

                # decrease-key(Q, v, d[v]) simulated by pushing the new value
                heapq.heappush(Q, (d[v], v))
                print("      Updated d['", v, "'] = ", d[v], ", parent['", v, "'] = '", u, "'. Pushed (", d[v], ", '", v, "') to Q.")
            else:
                print("      No relaxation needed for edge (", u, ",", v, "): Path through '", u, "' (", d[u] + weight, ") is not < current d['", v, "'] (", d[v], ")")

        print("current state: d=", d)
        print("Q after the pop:", Q)
        print("______________", iteration)

        

    print("Algo finished")
    return d, parent




print("Testing initialization")
dijkstra(G,s)


