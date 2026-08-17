import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            dist = x**2 + y**2

            heapq.heappush(heap, (dist, (x,y)))

        print(heap)

        points = []

        for i in range(k):
            points.append(heapq.heappop(heap)[1])

        return points
