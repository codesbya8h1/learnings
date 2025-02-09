# To determine if a partially completed Sudoku board is valid, we need to check the following:
# 	1.	Each row contains unique numbers between 1 and 9 (ignoring zeros).
# 	2.	Each column contains unique numbers between 1 and 9 (ignoring zeros).
# 	3.	Each of the nine 3×3 subgrids contains unique numbers between 1 and 9 (ignoring zeros).
def verify_sudoku_board(board):


    def is_valid_group(group):
        seen = set()
        for num in group:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True
    
    #check if the rows are valid
    for row in board:
        if not is_valid_group(row):
            return False
        

    #check if columns are valid
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False
        
    
    #check if all the subgrids are valid
    for box_row in range(0, 9, 3):
        for col_row in range(0, 9, 3):
            grid = [
                board[row][col] 
                for row in range(box_row, box_row+3)
                for col in range(col_row, col_row+3) 
            ]
            if not is_valid_group(grid):
                return False
    
    return True


    


# Example usage:
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]

print(verify_sudoku_board(sudoku_board))