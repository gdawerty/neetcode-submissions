class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        print(intervals)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = min(res[-1][1], intervals[i][1])

        

        return len(intervals) - len(res)