import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)


        while len(heap) > 1:
            a = -(heapq.heappop(heap))
            b = -(heapq.heappop(heap))

            diff = a - b

            if diff > 0:
                heapq.heappush(heap, -(a - b))

        if heap:
            return -heapq.heappop(heap)
        else:
            return 0
