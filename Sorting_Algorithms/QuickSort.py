def QuickSort(arr):
    if len(arr) == 1 or len(arr) == 0 :
        return arr 
    
    pivot =arr[-1]
    small=[x for x in arr[:-1] if x <= pivot]
    big = [x for x in arr[:-1] if x>pivot]
    
    return QuickSort(small) + [pivot] + QuickSort(big)

