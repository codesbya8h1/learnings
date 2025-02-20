# Maximums of Sliding Window
# Hard
# There's a sliding window of size k that slides through an integer array from left to right. Create a new array that records the largest number found in each window as it slides through.

# Example:


# Input: nums = [3, 2, 4, 1, 2, 1, 1], k = 4
# Output: [4, 4, 4, 2]

def max_sliding_window(nums, k):
    if not nums:
        return []
    
    window = []
    for i in range(len(nums)-k+1):
        window.append(max(nums[i:i+k]))
    
    return window

print(max_sliding_window([3, 2, 4, 1, 2, 1, 1], 4))
print(max_sliding_window([3, 2, 4, 1, 2, 1, 1], 3))