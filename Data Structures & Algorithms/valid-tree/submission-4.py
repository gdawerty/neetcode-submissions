class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        q = deque()

        q.appendleft([0, -1]) 
        

        while q:
            node, parent = q.popleft()
            if node in visited:
                return False

            visited.add(node)

            for nei in adj_list[node]:
                if nei == parent:
                    continue

                q.appendleft([nei, node])

        return len(visited) == n

