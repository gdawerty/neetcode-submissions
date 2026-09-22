import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        tasks_with_indices = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        sorted_tasks = sorted(tasks_with_indices, key=lambda x: x[0])
        i = 0
        time = 0
        res = []

        while heap or i < len(sorted_tasks):
            # 1. If heap is empty, jump time forward to sorted_tasks[i][0]
    # 2. Push all tasks whose arrival time <= time into the heap (advancing i)
    # 3. Pop the shortest task, append its index to res, and advance time
            if not heap:
                time = max(time, sorted_tasks[i][0])

            while i < len(sorted_tasks) and sorted_tasks[i][0] <= time:
                heapq.heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i += 1
            at, idx = heapq.heappop(heap)
            res.append(idx)

            time += at

        return res