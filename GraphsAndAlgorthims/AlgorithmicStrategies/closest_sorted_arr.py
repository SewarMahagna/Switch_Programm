"""Find in a sorted array the closest number to a given number"""
    
def get_closest_num_in_sorted_arr(arr, given_num):
    closest = arr[0]
    min_diff = abs(given_num - closest)
    for num in arr:
        diff = abs(given_num - num)
        if diff < min_diff:
            min_diff = diff
            closest = num

    return closest

arr = [100,120,125,145,158,179,184,185]
print(get_closest_num_in_sorted_arr(arr,150))

def get_closest_num_in_sorted_arr2(arr, given_num,closest =10^6):
    len_arr = len(arr)
    mid_indx = len_arr//2
    if given_num == arr[mid_indx] : 
        return given_num 
    if abs(given_num - arr[mid_indx]) > closest :
        return get_closest_num_in_sorted_arr2(arr[:mid_indx],given_num)
    if abs(given_num - arr[mid_indx]) < closest : 
        closest = given_num - arr[mid_indx]
        return get_closest_num_in_sorted_arr2(arr[mid_indx:],given_num)
    
