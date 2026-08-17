from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))

        # dist[city][steps] = min cost to reach `city` using exactly `steps` flights
        # You can use at most k stops => at most k + 1 flights
        max_steps = k + 1
        dist = [[float('inf')] * (max_steps + 1) for _ in range(n)]

        # start at src with 0 cost and 0 flights taken
        dist[src][0] = 0
        minHeap = [(0, src, 0)]  # (cost, node, steps)

        while minHeap:
            cost, node, steps = heapq.heappop(minHeap)

            # if we popped (node, steps) with cost > best known, skip
            if cost > dist[node][steps]:
                continue

            # if we reached destination within allowed steps, this is minimal cost
            if node == dst:
                return cost

            # can’t take more than max_steps flights
            if steps == max_steps:
                continue

            for nei, price in adj[node]:
                new_steps = steps + 1
                new_cost = cost + price
                if new_cost < dist[nei][new_steps]:
                    dist[nei][new_steps] = new_cost
                    heapq.heappush(minHeap, (new_cost, nei, new_steps))

        return -1
