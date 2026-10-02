class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        rows = len(heights)
        cols = len(heights[0])

        heap = [(0,0,0)]
        visited = [[False] * cols for _ in range(rows)]


        while heap:
            current_effort, row, col = heapq.heappop(heap)

            if row == rows - 1 and col == cols - 1:
                return current_effort

            if visited[row][col]:
                continue

            visited[row][col] = True

            # Check if you've reached the destination.

            for dx, dy in directions:
                nr, nc = row + dx, col + dy

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    diff = abs(heights[row][col] - heights[nr][nc])
                    new_effort = max(current_effort, diff)

                    heapq.heappush(heap, (new_effort, nr, nc))

        return 

        

