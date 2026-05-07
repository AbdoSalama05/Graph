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

# Test 1: Linear chain
# A → B → C → D
edges1 = {"A": ["B"], "B": ["C"], "C": ["D"], "D": []}
nodes1 = ["A", "B", "C", "D"]

# Test 2: Simple DAG
# A → C, B → C, C → D
edges2 = {"A": ["C"], "B": ["C"], "C": ["D"], "D": []}
nodes2 = ["A", "B", "C", "D"]

# Test 3: Independent paths
# A → B, C → D
edges3 = {"A": ["B"], "B": [], "C": ["D"], "D": []}
nodes3 = ["A", "B", "C", "D"]

# Test 4: Diamond
#     A
#    / \
#   B   C
#    \ /
#     D
edges4 = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
nodes4 = ["A", "B", "C", "D"]

# Test 5: Single node
edges5 = {"A": []}
nodes5 = ["A"]

# Test 6: No edges
edges6 = {"A": [], "B": [], "C": [], "D": []}
nodes6 = ["A", "B", "C", "D"]

all_tests = [
    (edges1, nodes1),
    (edges2, nodes2),
    (edges3, nodes3),
    (edges4, nodes4),
    (edges5, nodes5),
    (edges6, nodes6),
]

def build_graph(edges, nodes):
    index = {node: i for i, node in enumerate(nodes)}
    graph = [[] for _ in nodes]
    for src, dsts in edges.items():
        for dst in dsts:
            graph[index[src]].append(index[dst])
    return graph, index

for i, (edges, nodes) in enumerate(all_tests, 1):
    graph, index = build_graph(edges, nodes)
    order = topological_sort(graph)
    named = [nodes[i] for i in order]
    print(f"Test {i}: {named}")



