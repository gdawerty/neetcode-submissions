class TrieNode:
    def __init__ (self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = []
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        def dfs(row, col, node):
            char = board[row][col]

            if char not in node.children:
                return

            

            next_node = node.children[char]

            # found a complete word
            if next_node.word is not None:
                res.append(next_node.word)

                # prevents duplicate results
                next_node.word = None

            # mark visited
            board[row][col] = ""

            for dx, dy in directions:
                nr = row + dx
                nc = col + dy

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] != ""
                ):
                    dfs(nr, nc, next_node)

            # backtrack
            board[row][col] = char


        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return res