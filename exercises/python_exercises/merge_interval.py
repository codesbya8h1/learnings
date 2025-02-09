# Merge Overlapping Intervals
# Medium
# Merge an array of intervals so there are no overlapping intervals, and return the resultant merged intervals.

# Example:


# Input: intervals = [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]
# Output: [[1, 5], [6, 8]]
# Constraints:
# The input contains at least one interval.

# For every index i in the array, intervals[i].start ≤ intervals[i].end.
from typing import List

def merge_overlapping_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # Write your code here
    result = []

    intervals.sort(key=lambda x: x[0])
    # sorted_intervals = sorted(intervals, key=lambda x: x[0])
    # print(intervals)
    # print(sorted_intervals)

    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(interval[1], result[-1][1])


    return result


# Example usage
intervals = [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]
print(merge_overlapping_intervals(intervals))  # Output: [[1, 5], [6, 8]]