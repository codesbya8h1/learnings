# Given a 2D board of characters and an array of words, find all the words in the array that can be formed by tracing a path through adjacent cells in the board. Adjacent cells are those which horizontally or vertically neighbor each other. We can't use the same cell more than once for a single word.

# Example:


# Input: board = [['b', 'y', 's'], ['r', 't', 'e'], ['a', 'i', 'n']],
#        words = ['byte', 'bytes', 'rat', 'rain', 'trait', 'train']
# Output: ['byte', 'bytes', 'rain', 'train']
def display_board(board):
    for row in board:
        print(row)

def find_words(board, words):
    # Lets solve this problem using DFS
    # We will use a helper function to check if the word can be formed by tracing a path through adjacent cells in the board
    # We will use a visited set to keep track of the cells we have visited
    # We will use a result list to store the words that can be formed
    # We will use a helper function to check if the word can be formed by tracing a path through adjacent cells in the board
    result = []
    def dfs(board, word, row, col, visited):
        if len(word) == 0:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col]:
            return False
        if board[row][col] != word[0]:
            return False
        visited[row][col] = True
        res = dfs(board, word[1:], row+1, col, visited) or dfs(board, word[1:], row-1, col, visited) or dfs(board, word[1:], row, col+1, visited) or dfs(board, word[1:], row, col-1, visited)
        visited[row][col] = False
        print(word, i, j, visited, res)
        return res
    
    for word in words:
        for i in range(len(board)):
            for j in range(len(board[0])):
                # display_board(board)
                # print(word, i, j, [[False]*len(board[0]) for _ in range(len(board))])
                if dfs(board, word, i, j, [[False]*len(board[0]) for _ in range(len(board))]):
                    result.append(word)
    return result
    


board = [['b', 'y', 's'], ['r', 't', 'e'], ['a', 'i', 'n']]
words = ['byte', 'bytes', 'rat', 'rain', 'trait', 'train']

print(find_words(board, words))