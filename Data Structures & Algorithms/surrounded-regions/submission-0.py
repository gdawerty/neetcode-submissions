class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            seen.add((row,col))

            for dx, dy in directions:
                nr, nc = row + dx, col + dy

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and (nr, nc) not in seen:
                    dfs(nr, nc)

        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0) # left side
            if board[row][cols - 1] == 'O':
                dfs(row, cols - 1) # right side

        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0, col) # top side
            if board[rows - 1][col] == 'O':
                dfs(rows - 1, col) # bottom side

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row,col) not in seen:
                    board[row][col] = 'X'