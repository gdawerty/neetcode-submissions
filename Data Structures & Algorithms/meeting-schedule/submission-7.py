"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        

        intervals = sorted(intervals, key=lambda x: x.start)
        interval = intervals[0].end
        

        for i in range(1, len(intervals)):
            if intervals[i].start < interval:
                return False
            else:
                interval = intervals[i].end

        return True