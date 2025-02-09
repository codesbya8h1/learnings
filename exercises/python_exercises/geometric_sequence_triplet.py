# Geometric Sequence Triplets
# Medium
# A geometric sequence triplet is a sequence of three numbers where each successive number is obtained by multiplying the preceding number by a constant called the common ratio.

# Let's examine three triplets to understand how this works:

# (1, 2, 4): This is a geometric sequence with a ratio of 2 (i.e., [1, 1⋅2 = 2, 2⋅2 = 4]).
# (5, 15, 45): This is a geometric sequence with a ratio of 3 (i.e., [5, 5⋅3 = 15, 15⋅3 = 45]).
# (2, 3, 4): Not a geometric sequence.
# Given an array of integers and a common ratio r, find all triplets of indexes (i, j, k) that follow a geometric sequence for i < j < k. It's possible to encounter duplicate triplets in the array.

# Example:


# Input: nums = [2, 1, 2, 4, 8, 8], r = 2
# Output: 5
# Explanation:

# Triplet [2, 4, 8] occurs at indexes (0, 3, 4), (0, 3, 5), (2, 3, 4), (2, 3, 5).
# Triplet [1, 2, 4] occurs at indexes (1, 2, 3).

def count_geometric_triplets(nums, r):
    """
    Count all geometric sequence triplets in nums with common ratio r.
    
    :param nums: List[int] - Input array
    :param r: int - Common ratio
    :return: int - Number of valid geometric triplets
    """
    count_map = {}  # Tracks potential second elements of geometric sequences
    triplet_map = {}  # Tracks potential third elements of geometric sequences
    count = 0  # Total count of valid triplets

    for num in nums:
        # If num is the third element of a triplet, add its count to the total
        if num in triplet_map:
            count += triplet_map[num]

        # If num is the second element of a potential triplet, update triplet_map
        if num in count_map:
            next_num = num * r
            if next_num not in triplet_map:
                triplet_map[next_num] = 0
            triplet_map[next_num] += count_map[num]

        # Add num as a potential first element for future sequences
        next_num = num * r
        if next_num not in count_map:
            count_map[next_num] = 0
        count_map[next_num] += 1

        print("triplet_map :",triplet_map)
        print("count_map :",count_map)
        print("count : ",count)

    return count

# Example Usage
nums = [2, 1, 2, 4, 8, 8]
r = 2
print(count_geometric_triplets(nums, r))  # Output: 5