class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, cost in flights:
            adj[u].append([v, cost])

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        
        minHeap = [(0, src, -1)]

        while minHeap:
            cost, node, stop = heapq.heappop(minHeap)

            if node == dst and stop <= k:
                return cost

            if stop == k:
                continue

            for nei, edge in adj[node]:
                next_edge = edge + cost
                next_stops = 1 + stop

                if next_edge < dist[nei][next_stops]:
                    dist[nei][next_stops] = next_edge
                    heapq.heappush(minHeap, (next_edge, nei, next_stops))

        return -1