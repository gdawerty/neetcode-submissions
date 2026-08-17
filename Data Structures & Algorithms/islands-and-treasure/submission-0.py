class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #scan grid
        #perform bfs

        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        while queue:
            row, col = queue.popleft()

            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))