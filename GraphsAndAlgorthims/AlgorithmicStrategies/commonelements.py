#Brute Force Solution  : Nested Loop (All The Options) ==> Not Efficient
def CommonElements(arr1,arr2):
    common_arr = []
    for element1 in arr1 : 
        for element2 in arr2 : 
            if  element1 == element2 and element1 not in common_arr : 
                common_arr.append(element1)

    return common_arr 

def count_common(arr): 
    count_dic = {}
    for element in arr:
        if count_dic.get(element):
            count_dic[element] += 1  
        else:
            count_dic[element] = 1  
    return count_dic

def Commons_of_two(arr1,arr2): 
    common_dic1 = count_common(arr1) 
    common_dic2 = count_common(arr2)
    common_lst = []
    for key in common_dic1 : 
        if common_dic2.get(key) :
            common_lst.append(key)
    return common_lst

def commons_of_three(arr1,arr2,arr3):
    common_dic1 = count_common(arr1) 
    common_dic2 = count_common(arr2)
    common_dic3 = count_common(arr3)
    common_lst = []
    for key in common_dic1 : 
        if common_dic2.get(key)  and common_dic3.get(key) :
            common_lst.append(key)
    return common_lst



arr1 = [2,3,5,8,2,1,4,9,7,6,5,4,2,3]
arr2 = [2,1,4,8,9,7,10,11,12,14,5,7,6,2]
arr3 = [5,14,19,8,15,2,3,7,4,8,9]
#print(Commons_of_two(arr1,arr2))
print(commons_of_three(arr1,arr2,arr3))