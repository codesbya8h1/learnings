def longest_consecutive_sequence(nums):
    if not nums:
        return []
    
    nums_set = set(nums)
    max_lenght = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            curr_num = num
            curr_length = 1

            while curr_num+1 in nums_set:
                curr_num +=1
                curr_length+=1
            
            max_lenght = max(curr_length, max_lenght)
        
    return max_lenght


# Example usage:
L = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(L))  # Output: 4 (sequence: [1, 2, 3, 4])

L = [10, 5, 12, 3, 55, 30, 4, 11]
print(longest_consecutive_sequence(L))  # Output: 3 (sequence: [10, 11, 12])