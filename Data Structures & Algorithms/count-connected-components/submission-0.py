class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        components = 0

        def bfs(node):
            queue = deque()
            queue.append(node)
            visited[node] = True

            while queue:
                curr = queue.popleft()

                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)



        for node in range(n):
            if not visited[node]:
                components+=1
                bfs(node)

        return components

