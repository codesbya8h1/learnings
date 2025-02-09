from typing import List

# Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order of non-zero elements.

# Example:
# Input: nums = [0, 1, 0, 3, 2]
# Output: [1, 3, 2, 0, 0]

def shift_zeros_to_the_end(nums: List[int]) -> None:
    # Write your code here
    non_zero_index = 0

    for i in range(len(nums)):
        print(i, ":", nums)
        if nums[i]!=0:
            #swap
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

    print("Final : ",nums)

nums = [0, 1, 0, 3, 2]
print(shift_zeros_to_the_end(nums))

