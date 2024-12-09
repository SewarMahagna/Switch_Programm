graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G':[]
}

def print_dfs(graph,node,visited=None):
    if visited is None:
        visited = []
        
    if node not in visited:
        print(f"node:{node}")
        visited.append(node)

    for child in graph[node]:
        print_dfs(graph, child, visited)

print_dfs(graph,'A')
        