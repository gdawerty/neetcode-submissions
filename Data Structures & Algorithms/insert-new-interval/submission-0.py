class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        res = []
        did_add = False


        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                if not did_add:
                    res.append(newInterval)
                    did_add = True
                res.append(interval)
            else:
                new_start = min(interval[0], newInterval[0])
                new_end = max(interval[1], newInterval[1])
                newInterval[0] = new_start
                newInterval[1] = new_end


        if not did_add:
            res.append(newInterval)

        return res




