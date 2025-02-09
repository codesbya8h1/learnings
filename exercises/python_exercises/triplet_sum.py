from typing import List

# Input: nums = [0, -1, 2, -3, 1]
# Output: [[-3, 1, 2], [-1, 0, 1]]

def triplet_sum(nums: List[int]) -> List[List[int]]:
    # Write your code here
    # Sort the array
    nums.sort()
    result = []
    print(nums)
    
    # Iterate through the array
    for i in range(len(nums)):
        # Skip duplicate values for `a`
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two-pointer approach
        left, right = i + 1, len(nums) - 1
        while left < right:
            print(nums[i], nums[left], nums[right])
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for `b` and `c`
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move pointers
                left += 1
                right -= 1
            elif total < 0:
                # Increase sum by moving left pointer
                left += 1
            else:
                # Decrease sum by moving right pointer
                right -= 1
    
    return result



nums = [-4,-4,-2,0,0,1,2,3]
nums = [0, -1, 2, -3, 1]
print(triplet_sum(nums))