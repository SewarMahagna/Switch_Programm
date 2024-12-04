from MergeSort import MergeSort

def Merge_Absolute(arr):
    arr = [abs(element) for element in arr ]
    return MergeSort(arr)

def SortCapLow(string):
    new_string = [ord(element) for element in string]
    sorted_assci_values = MergeSort(new_string)
    result_string = ''.join(chr(value) for value in sorted_assci_values)
    return result_string

def SortOddEven(arr): 
    odd = [element for element in arr if element%2==1]
    even =[element for element in arr if element%2==0]

    odd = MergeSort(odd)
    even = MergeSort(even)
    odd.extend(even)
    return odd

def SortPrimeRest(arr):
    prime = [element for element in arr if is_prime(element)]
    rest = [element for element in arr if not is_prime(element)]
    prime = MergeSort(prime)
    rest=MergeSort(rest)
    prime.extend(rest)
    return prime 

def is_prime(num):
    if num == 1 or num == 2 : 
        return True
    if num %2 == 0:
        return False
    up_to=int(num**0.5) + 1
    index = 3 
    while index <= up_to : 
        if num % index ==0 and num != index  :
            return False 
        index+=1 
    return True
    
test1 = Merge_Absolute([100,-1,-2,5,9,3,0,5])
#print(test1)

test2 = SortCapLow("HelLOmYnamEISsewar")
#print(test2)

test3 = SortOddEven([2,4,8,6,4,1,3,7,10,3,5,0,9])
#print(test3)

test4 = SortPrimeRest([1,5,17,8,2,6,94,2,1,3,9,18,100,20])
print(test4)