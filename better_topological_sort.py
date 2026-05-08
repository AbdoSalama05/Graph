from collections import deque

def kahn(graph):
    n = len(graph)
    index = 0

    indegree = {node: 0 for node in graph}
    result = []
    q = deque()

    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    for node in graph:
        if(indegree[node]==0):
            q.append(node)
    
    while q:
        top = q.popleft()
        result.append(top)
        index += 1

        for neighbour in graph[top]:
            indegree[neighbour] -= 1
            if(indegree[neighbour] == 0):
                q.append(neighbour)
    
    if(index != n):
        print("Cycle detected")
        return None

    return result

graph = {
    7: [5, 6],
    5: [2, 4],
    6: [4, 3],
    4: [1],
    2: [],
    3: [],
    1: [0],
    0: []
}

result = kahn(graph)
print("Topological Sort using Kahn's algorithm:", result)