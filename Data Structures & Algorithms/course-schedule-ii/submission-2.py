class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] +=1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        res = []

        while queue:
            curr = queue.popleft()
            res.append(curr)

            for neighbor in adj_list[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return res if len(res) == numCourses else []