# Longest Chain of Consecutive Numbers
# Medium
# Find the longest chain of consecutive numbers in an*array. Two numbers are consecutive if they have a difference of 1.

# Example:
# Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
# Output: 4
# Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.

def longest_consecutive_chain(nums):

    if not  nums:
        return []
    

    result = []
    nums.sort()
    print(nums)

    current_list = [nums[0]]

    for i in range(1, len(nums)):
        
        if nums[i] - nums[i - 1] == 1:  # Check if consecutive
            current_list.append(nums[i])
            print(current_list)
        elif nums[i] != nums[i - 1]:  # Handle duplicates (skip them)
            # Update result if the current chain is longer
            if len(current_list) > len(result):
                result = current_list
                print(result)
            current_list = [nums[i]]  # Start a new chain
    
    # Final check to update the result after the loop
    if len(current_list) > len(result):
        result = current_list

        

    return result

nums = [1, 6, 2, 5, 8, 7, 10, 3]
print(longest_consecutive_chain(nums))