import heapq
from collections import defaultdict, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        freq = defaultdict(int)

        for task in tasks:
            freq[task] += 1

        
        heap = []
        time = 0

        for task in freq.values():
            heapq.heappush(heap, -task)

        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt < 0:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time    