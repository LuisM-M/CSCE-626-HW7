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


while len(list1) > 1:
    print(heapq.heappop(list1))