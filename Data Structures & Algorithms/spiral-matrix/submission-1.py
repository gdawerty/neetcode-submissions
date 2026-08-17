class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []

        # directions: right, down, left, up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        VISITED = "#"

        def dfs(r, c, dir_idx, visited_count):
            # base case: visited all cells
            if visited_count == rows * cols:
                return

            # 1) visit current cell
            res.append(matrix[r][c])
            matrix[r][c] = VISITED

            # 2) try to go straight in same direction
            dr, dc = dirs[dir_idx]
            nr, nc = r + dr, c + dc

            # helper to check bounds + not visited
            def valid(x, y):
                return 0 <= x < rows and 0 <= y < cols and matrix[x][y] != VISITED

            if valid(nr, nc):
                dfs(nr, nc, dir_idx, visited_count + 1)
            else:
                # 3) turn right (change direction)
                new_dir = (dir_idx + 1) % 4
                dr, dc = dirs[new_dir]
                nr, nc = r + dr, c + dc
                if valid(nr, nc):
                    dfs(nr, nc, new_dir, visited_count + 1)
                else:
                    # nowhere to go -> done
                    return

        dfs(0, 0, 0, 0)  # start at (0,0), moving right (dir_idx 0), visited_count = 0
        return res
