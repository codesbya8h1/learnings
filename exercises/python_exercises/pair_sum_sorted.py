from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    # Input: nums = [-5, -2, 3, 4, 6], target = 7
    # Output: [2, 3]
    result =[]
    j = len(nums)-1
    i = 0
    while i < j:
        print(nums[i], nums[j])
        if nums[i] + nums[j] == target:
            result.append(i)
            result.append(j)
            break
        if nums[i] + nums[j] > target:
            j = j-1
        if nums[i]+nums[j] < target:
            i = i+1

    return result

nums = [-5, -2, 3, 4, 6]
target = 7
print(pair_sum_sorted(nums, 7))