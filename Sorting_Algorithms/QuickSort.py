def QuickSort(arr):
    if len(arr) == 1 or len(arr) == 0 :
        return arr 
    
    pivot =arr[-1]
    small=[x for x in arr[:-1] if x<= pivot]
    big = [x for x in arr[:-1] if x>pivot]
    
    return QuickSort(small) + [pivot] + QuickSort(big)

test = QuickSort([23,6,3,8,7,1,2,5,4,9,10,11,10,8,9,10,100,10])
print(test)