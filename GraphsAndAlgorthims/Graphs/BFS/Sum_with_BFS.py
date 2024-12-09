number_graph = {
    3:[1,5,8],
    4: [2],
    1: [9,6],
    5: [],
    8: [7],
    7:[4],
    9: [],
    6:[],
    2: []
}

def Sum_all_bfs(graph, start_node):
    queue = [start_node] 
    visited_nodes = [] 
    sum = 0    
    while len(queue) > 0: 
        current_node = queue.pop(0)  
        if current_node not in visited_nodes:
            sum += int(current_node)
            visited_nodes.append(current_node)
            for neighbor in graph[current_node]: 
                queue.append(neighbor)
    return sum 

def Sum_odd_bfs(graph, start_node):
    queue = [start_node] 
    visited_nodes = [] 
    sum = 0    
    while len(queue) > 0: 
        current_node = queue.pop(0)  
        if current_node not in visited_nodes:
            if current_node%2==1:
                sum += int(current_node)
            visited_nodes.append(current_node)
            for neighbor in graph[current_node]: 
                queue.append(neighbor)
    return sum 

def Sum_even_bfs(graph, start_node):
    queue = [start_node] 
    visited_nodes = [] 
    sum = 0    
    while len(queue) > 0: 
        current_node = queue.pop(0)  
        if current_node not in visited_nodes:
            if current_node%2==0:
                sum += int(current_node)
            visited_nodes.append(current_node)
            for neighbor in graph[current_node]: 
                queue.append(neighbor)
    return sum 

print(Sum_all_bfs(number_graph,3))
print(Sum_odd_bfs(number_graph,3))
print(Sum_even_bfs(number_graph,3))