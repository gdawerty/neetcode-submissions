class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        def dfs(row, col):
            grid[row][col] = '2'

            for direction in directions:
                if 0<= row + direction[0]< len(grid) and 0<= col + direction[1]< len(grid[0]) and grid[row + direction[0]][col + direction[1]] == '1':
                    dfs(row + direction[0], col + direction[1])



        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count+=1

        return count

        