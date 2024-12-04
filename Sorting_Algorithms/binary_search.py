
def binary_search(lst,number):
    len_of_lst = len(lst)
    index_of_mid =len_of_lst//2 
    mid_num = lst[index_of_mid]
    rigth = index_of_mid+1
    left = index_of_mid-1 
    if number == mid_num : 
        return index_of_mid
    elif number > mid_num:
        return binary_search(lst[rigth:],number)
    elif number < mid_num:
        return binary_search(lst[:left],number)



lst = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]

print(binary_search(lst,37))