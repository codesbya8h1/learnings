# Given an integer array and number k, output all unique pairs that sum up to k. 
# Example: for input [1, 3, 2, 5, 46, 6, 7, 4] and k = 4, output (1, 3).

# Give me a code for above problem using binary search.

def binary_search(nums, target, left, right):
    

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


def find_all_sum_of_two(nums, target):
    result= []
    if not nums:
        return result
    
    nums.sort()
    n  = len(nums)
    result = set()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        complement = target - nums[i]
        if binary_search(nums, complement, i+1, n-1):
            result.add((nums[i], complement))

    return list(result)

nums = [1,3,2,5,46,6,7,4]
k = 4
print(find_all_sum_of_two(nums, k))
