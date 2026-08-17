import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        val = 0
        for i in range(k):
            val = -heapq.heappop(heap)

        return val