class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])

        atlantic_list = set()
        pacific_list = set()

        res = []

        directions = [[0,1], [0,-1], [1,0], [-1,0]]


        def dfs(row, col, lists, prev):
            if not (0 <= row < rows) or not (0 <= col < columns) or prev > heights[row][col] or (row,col) in lists:
                return

            lists.add((row, col))

            for dx, dy in directions:
                dfs(row + dx, col + dy, lists, heights[row][col])


        for row in range(rows):
            dfs(row, 0, pacific_list, 0) #left side
            dfs(row, columns - 1, atlantic_list, 0) #right side

        for col in range(columns):
            dfs(0, col, pacific_list, 0) #top side
            dfs(rows - 1, col, atlantic_list, 0) #bottom side
        
        for val in atlantic_list:
            if val in pacific_list:
                res.append(val)

        return res