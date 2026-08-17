class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * (len(edges) + 1)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue = deque()

        for i in range(1, len(edges) + 1):
            if indegree[i] == 1:
                queue.append(i)

        print(indegree)
        while queue:
            curr = queue.popleft()
            indegree[curr] -=1
            for nei in adj_list[curr]:
                indegree[nei] -=1

                if indegree[nei] == 1:
                    queue.append(nei)

        
 
        for u, v in reversed(edges):
            if indegree[v] == 2 and indegree[u] >= 1:
                return [u, v]
        return []

