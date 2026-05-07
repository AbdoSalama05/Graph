import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # weight,node,parent
    mst = []
    total_cost = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        total_cost += weight

        if parent is not None:
            mst.append((parent, u, weight))

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))

    # Check connectivity
    if len(visited) != len(graph):
        print("Graph is not connected, MST cannot be formed")
        return None, None

    return mst, total_cost


graph = {
    'a': [('b',4), ('h',8)],
    'b': [('a',4), ('c',8)],
    'c': [('b',8), ('d',7), ('i',2), ('f',4)],
    'd': [('c',7), ('e',9), ('f',14)],
    'e': [('d',9), ('f',10)],
    'f': [('e',10), ('d',14), ('c',4), ('g',2)],
    'g': [('f',2), ('h',1), ('i',6)],
    'h': [('a',8), ('g',1), ('i',7)],
    'i': [('c',2), ('h',7), ('g',6)]
}

mst, cost = prim(graph, 'a')
if mst:
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")

    print("Total cost:", cost)