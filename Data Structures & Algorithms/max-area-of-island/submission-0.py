class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] != 1:
                return 0

            grid[row][col] = 2
            area = 1
            
            for dx, dy in directions:
                area += dfs(row + dx, col + dy)

            return area

            

        max_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count = dfs(row, col)
                    max_count = max(max_count, count)

        return max_count

