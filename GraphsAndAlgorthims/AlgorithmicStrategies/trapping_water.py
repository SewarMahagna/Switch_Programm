#bruteForce Solution O(n^2)
def trappedWater(arr):
    output_result = 0
    for i in range(len(arr)):
        max_left_building = arr[i]   
        max_right_building = arr[i]  

        for j in range(i):  
            max_left_building = max(max_left_building, arr[j])

        for j in range(i + 1, len(arr)):  
            max_right_building = max(max_right_building, arr[j])

        output_result += max(0, min(max_left_building, max_right_building) - arr[i])

    return output_result

arr =[3, 0, 1, 0, 4, 0, 2]
print(trappedWater(arr))
        