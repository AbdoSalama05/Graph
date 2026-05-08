def dfs(visited,index, graph, result):
    visited[index] = True
    for i in graph[index]:
        if(not visited[i]):
            dfs(visited,i,graph, result)

    result.append(index)

def topological_sort(graph):
    visited = [False] * len(graph)
    sorted_result = []
    for i in range(len(graph)):
        if(not visited[i]):
            dfs(visited, i, graph, sorted_result)
    sorted_result = list(reversed(sorted_result))
    return sorted_result


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

result = topological_sort(graph)
print("Topological Sort:", result)

