# Pair Sum - Unsorted
# Easy
# Given an array of integers, return the indexes of any two numbers that add up to a target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

# Example:
# Input: nums = [-1, 3, 4, 2], target = 3
# Output: [0, 2]
# Explanation: nums[0] + nums[2] = -1 + 4 = 3

# Constraints:
# The same index cannot be used twice in the result.

from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    # Dictionary to store numbers and their indices
    seen = {}
    
    for i, num in enumerate(nums):
        print(i , seen, target, num)

        # Calculate complement
        complement = target - num
        
        # Check if complement exists in the hashmap
        if complement in seen:
            return [seen[complement], i]
        
        # Add current number to hashmap
        seen[num] = i
    
    # No pair found
    return []

# Example usage
nums = [-1, 3, 4, 2]
target = 3
print(pair_sum_unsorted(nums, target))  # Output: [0, 2]