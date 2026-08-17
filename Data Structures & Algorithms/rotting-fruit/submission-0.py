class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col,0))

        max_val = 0
        while queue:
            row, col, minute = queue.popleft()

            for dx, dy in directions:
                nr, nc = row + dx, col + dy

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    max_val = max(max_val, minute + 1)
                    queue.append((nr,nc,minute + 1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return max_val

