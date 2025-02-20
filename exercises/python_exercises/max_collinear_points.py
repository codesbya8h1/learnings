# Given a set of points in a two-dimensional plane, determine the maximum number of points that lie along the same straight line.

# Example:


# Input: points = [[1, 1], [1, 3], [2, 2], [3, 1], [3, 3], [4, 4]]
# Output: 4

from typing import List
from math import gcd
def maximum_collinear_points(points: List[List[int]]) -> int:
    # Write your code here
    
    
    def get_slope(point1, point2):
        dx = point2[0]-point1[0]
        dy = point2[1]-point1[1]

        if dx == 0:
            return ('inf', 0)
        if dy == 0:
            return (0, 'inf')
        
        d = gcd(dx, dy)
        return (dy // d, dx // d)

    n = len(points)
    if n <= 2:
        return n

    max_collinear = 0
    for i in range(n):
        slope_map = {}  
        for j in range(n):
            if i!=j:
                slope = get_slope(points[i], points[j])
                slope_map[slope] = slope_map.get(slope, 0) + 1
                print(slope_map)
        max_collinear = max(max_collinear, max(slope_map.values(), default=0) + 1)
    
    
    return max_collinear


        

points = [[1, 1], [1, 3], [2, 2], [3, 1], [3, 3], [4, 4]]
print(maximum_collinear_points(points))

