import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges_used = 0
        visited = [False] * len(points)

        def dist(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            return abs(x1 - x2) + abs(y1 - y2)

        total = 0

        min_heap = [(0,0)] # cost, node
        heapq.heapify(min_heap)

        while edges_used < len(points):
            cost, node = heapq.heappop(min_heap)

            if visited[node]:
                continue

            visited[node] = True

            total += cost
            edges_used +=1

            for v in range(len(points)):
                if not visited[v]:
                    new_cost = dist(node, v)
                    heapq.heappush(min_heap, (new_cost, v))

        return total

