class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        directions = [[0,1],[-1,0],[1,0],[0,-1]]

        def dfs(row, col, i):

            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] != word[i]:
                return False
            
            if i == len(word) - 1:
                return True
            
            temp = board[row][col]
            board[row][col] = "#"

            for dx, dy in directions:
                if dfs(row + dx, col + dy, i + 1):
                    return True
            
            board[row][col] = temp
            
            return False



        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False