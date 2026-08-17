class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, cost in flights:
            adj[u].append([v, cost])

        dist = [[float('inf')] * n for _ in range(n)]

        minHeap = [(0, src, -1)] #cost, node, stop

        while minHeap:
            cost, node, stop = heapq.heappop(minHeap)

            if node == dst:
                return cost

            if stop == k or cost > dist[node][stop]:
                continue

            for nei, price in adj[node]:
                new_edge = price + cost
                new_stop = stop + 1

                if dist[nei][new_stop] > new_edge:
                    dist[nei][new_stop] = new_edge
                    heapq.heappush(minHeap, (new_edge, nei, new_stop))

        return -1