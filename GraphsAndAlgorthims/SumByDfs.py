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

def sum_all_by_dfs(number_graph, node, visited=None, total_sum=0):
    if visited is None:
        visited = []
        
    if node not in visited:
        visited.append(node)
        total_sum += int(node)
        
    for child in number_graph[node]:
        total_sum = sum_all_by_dfs(number_graph, child, visited, total_sum)
        
    return total_sum

def sum_odd_by_dfs(number_graph, node, visited=None, total_sum=0):
    if visited is None:
        visited = []
        
    if node not in visited :
        visited.append(node)
        if int(node) %2 ==1 : 
            total_sum += int(node)
        
    for child in number_graph[node]:
        total_sum = sum_odd_by_dfs(number_graph, child, visited, total_sum)
        
    return total_sum


def sum_even_by_dfs(number_graph, node, visited=None, total_sum=0):
    if visited is None:
        visited = []
        
    if node not in visited :
        visited.append(node)
        if int(node) %2 ==0: 
            total_sum += int(node)
        
    for child in number_graph[node]:
        total_sum = sum_even_by_dfs(number_graph, child, visited, total_sum)
        
    return total_sum


print(sum_even_by_dfs(number_graph, 3))
