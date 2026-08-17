import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False] * (n + 1)
        adj_list = defaultdict(list)
        total = 0

        for u, v, time in times:
            adj_list[u].append((time, v))

        min_heap = [(0, k)]
        heapq.heapify(min_heap)

        nodes_visited = 0

        while nodes_visited < n and min_heap:
            curr_time, node = heapq.heappop(min_heap)

            total = max(total, curr_time)

            if visited[node]:
                continue

            visited[node] = True
            nodes_visited +=1

            for time, nei in adj_list[node]:
                heapq.heappush(min_heap, (time + curr_time, nei))

        return total if nodes_visited == n else -1