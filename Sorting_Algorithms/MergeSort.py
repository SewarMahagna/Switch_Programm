def MergeSort(arr):
    len_arr = len(arr)
    if len_arr < 2 : 
        return arr
    elif len(arr) == 2 : 
        swip = arr[0]
        if arr[0] > arr[1]:
            arr[0] = arr[1]
            arr[1] = swip
        return arr 
    else:
        mid_index = len_arr//2 
        left = MergeSort(arr[:mid_index])
        right =MergeSort(arr[mid_index:])
        return Merge(left,right,arr)

def Merge(left, right, arr):
    i = j = k = 0  
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr








    
    

