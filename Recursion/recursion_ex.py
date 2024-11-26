def fibonacci_sequence(index):
    if index == 0 : 
        return 0 
    if index == 1:
        return 1 
    return fibonacci_sequence(index-1) + fibonacci_sequence(index-2)


print(fibonacci_sequence(6))


def find_subset(lst):
    if not lst : 
        return [[]]
    
    first_element = lst[0]
    rest_subsets = find_subset(lst[1:])
    
    new_subsets = []
    for subset in rest_subsets:
        new_subsets.append(subset + [first_element])
    
    return rest_subsets + new_subsets
    

print(find_subset([1,2,3]))
