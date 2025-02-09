# Zero Striping
# For each zero in an m x n matrix, set its entire row and column to zero in place.

def set_zeroes(matrix):
    """
    Modify the matrix such that if any cell contains 0, its entire row and column are set to 0.
    This is done in-place with O(1) additional space.
    """

    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                if i == 0:
                    first_row_zero = True
                if j == 0:
                    first_col_zero = True
                
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set all the rows to zero

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    

    # handle the first row and column separately
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


        


# Example Usage
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

set_zeroes(matrix)
print(matrix)
