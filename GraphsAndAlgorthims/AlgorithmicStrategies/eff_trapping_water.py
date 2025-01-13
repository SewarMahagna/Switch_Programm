def trappedWater2(arr): 

    arr_len = len(arr)
    output_result =0 

    max_left =[0]*arr_len 
    max_right = [0]*arr_len 

    max_left[0]= arr[0]
    for i in range(1,arr_len ): 
        max_left[i] = max(max_left[i-1],arr[i])
    print("max left list : ",max_left)

    max_right[arr_len-1] = arr[arr_len-1]
    for j in range(arr_len-2,-1,-1):
        max_right[j] = max(arr[j],max_right[j+1])
    print("max right list : ",max_right)

    for k in range(arr_len): 
        output_result +=( min(max_left[k], max_right[k]) - arr[k])
    
    return output_result

arr =[3, 0, 1, 0, 4, 0, 2]
print("Result :",trappedWater2(arr))
