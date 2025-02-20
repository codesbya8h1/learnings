# Here's the task: you've been given a 2D matrix consisting of individual cells, each holding a unique integer value. Your goal is to create a function that will traverse this matrix, starting at the bottom right cell. From there, you'll travel up to the top of the same column, then move left to the next column, and then continue downwards from the top of this new column. After reaching the bottom of the column, you again move left and start moving upwards. This unique traverse pattern will be performed until all the cells have been visited.

# Consider this small 
# 3
# ×
# 4
# 3×4 matrix as an example:

# Python
# Copy to clipboard
# Play
# [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# With the described traversal pattern, your function should return this list: [12, 8, 4, 3, 7, 11, 10, 6, 2, 1, 5, 9]

# brute force solution
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
zig_zag = []
row = 2
col = 3
while col >= 0:
    if row == 2:
        for i in range(2, -1, -1):
            zig_zag.append(array[i][col])
        col = col - 1
        row = 0
    elif row == 0:
        for i in range(3):
            zig_zag.append(array[i][col])
        col = col - 1
        row = 2
    
print(zig_zag)
    
# optimized solution
def traverse_matrix(matrix):
    result = []
    rows, cols = len(matrix), len(matrix[0])
    direction = 'up'
    row, col = rows-1, cols-1
    result = []
    while len(result) < rows * cols:
        result.append(matrix[row][col])

        if direction == 'up':
            if row-1 <  0:
                col -= 1
                direction = 'down'
            else:
                row -= 1
        else:
            if row + 1 == rows:
                col -= 1
                direction = 'up'
            else:
                row += 1

    return result

matrix = array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print("Optimized solution...")
print(traverse_matrix(matrix))