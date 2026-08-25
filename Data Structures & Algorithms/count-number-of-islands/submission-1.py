class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        res = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    res +=1
                    self.dfs(row, col, rows, cols, grid, directions)
                    

        return res

    def dfs(self, row, col, rows, cols, grid, directions) -> None:

        
        grid[row][col] = '0'

        for dx, dy in directions:
            if (0 <= row + dx< rows) and (0 <= col + dy< cols) and grid[row + dx][col + dy] == '1':
                self.dfs(row + dx, col + dy, rows, cols, grid, directions)

        return