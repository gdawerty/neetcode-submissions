class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = []
        for i in range(10000):
            visited.append(i)
        max_area = 0

        def dfs(row: int, col: int):
            area = 1
            for dx, dy in directions:
                if 0 <= row + dx < rows and 0 <= col + dy < cols and grid[row + dx][col + dy] == 1:
                    grid[row + dx][col + dy] = 0
                    
                    area += dfs(row + dx, col + dy)

            return area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    max_area = max(max_area, dfs(row, col))

        return max_area