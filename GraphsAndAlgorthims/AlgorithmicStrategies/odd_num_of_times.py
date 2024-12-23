"""Odd number of times  

Given an array, find the int that appears an odd number of times."""

def get_frequencies(arr): 
    dic_of_frequencies = {}
    for element in arr:
        if dic_of_frequencies.get(element):
            dic_of_frequencies[element] += 1  
        else:
            dic_of_frequencies[element] = 1  
    return dic_of_frequencies

def get_odd_num_of_times(arr):
    common_int_dic = get_frequencies(arr)
    for element in arr : 
        frequencies = common_int_dic.get(element) % 2
        if frequencies % 2 == 1 : 
            return element
    return "No number appears an odd number of times."

array = [1,2,1,2,3,6,8,7,9,7,7,1,5,5,1]
print(get_odd_num_of_times(array))
