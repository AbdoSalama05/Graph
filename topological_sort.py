def topological_sort(graph, node):
    sorted = []
    visited = len(graph)*[False]

    for i in range(len(graph)):
        if not visited[i]:
               dfs(i)
