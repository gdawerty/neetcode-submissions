class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        adj_list = defaultdict(list) #create mapping of courses

        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] +=1

        queue = deque()

        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)

        taken = 0

        while queue:
            curr = queue.popleft()
            taken+=1

            for nxt in adj_list[curr]:
                indegree[nxt]-=1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return True if taken == numCourses else False