graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G':[]
}

def print_bfs(graph, start_node):
    queue = [start_node] 
    visited_nodes = []    
    while len(queue) > 0: 
        current_node = queue.pop(0)  
        if current_node not in visited_nodes:
            print(current_node)
            visited_nodes.append(current_node)
            for neighbor in graph[current_node]: 
                queue.append(neighbor)


print_bfs(graph , "A")