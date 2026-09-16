class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            

            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                if 0 <= nr < rows and 0 <= nc < cols and idx <= len(word) and word[idx] == board[nr][nc]:
                    temp = board[nr][nc]
                    board[nr][nc] = ""
                    if dfs(nr, nc, idx + 1):
                        return True
                    board[nr][nc] = temp
                
            return False



        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    temp = board[row][col]
                    board[row][col] = ""
                    res = dfs(row, col, 1)
                    if res:
                        return True
                    
                    board[row][col] = temp

        return False