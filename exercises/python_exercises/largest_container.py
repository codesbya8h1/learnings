from typing import List

def largest_container(heights: List[int]) -> int:
    # Write your code here
    
    left = 0 
    right = len(heights) - 1
    max_area = 0 

    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        current_area = height * width

        max_area = max(max_area, current_area)

        if heights[left] < heights[right]:
            left = left + 1
        else:
            right = right - 1
    
    
    return max_area




# Input: heights = [2, 7, 8, 3, 7, 6]
# Output: 24

heights = [2, 7, 8, 3, 7, 6]
print(largest_container(heights))