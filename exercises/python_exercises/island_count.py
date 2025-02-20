from collections import deque
def count_islands(grid):    

    if not grid:
        return 0
    
    def bfs(row, col):
        q = deque()
        visited.add((row, col))
        q.append((row, col))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            row, col = q.popleft()
            

            for dr, dc in directions:
                row, col = row+dr, col+dc

                if (row in range(rows) and col in range(cols)  and grid[row][col] == '1'  and (row, col) not in visited ):
                    q.append((row, col))
                    visited.add((row, col))

    
    
    
    count = 0    
    rows  = len(grid)
    cols = len(grid[0])
    visited = set()


    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' and (row, col) not in visited:
                bfs(row, col)
                count+=1

    return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(count_islands(grid))