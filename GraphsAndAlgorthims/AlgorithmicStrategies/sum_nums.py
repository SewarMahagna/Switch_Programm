

def twoSum(nums, target):
    seen_in_arr = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen_in_arr:
            return [seen_in_arr[diff], i]
        else:
            seen_in_arr[nums[i]] = i
    return []


nums = [2,8,6,3,7,9,1,5]
print(twoSum(nums ,9))