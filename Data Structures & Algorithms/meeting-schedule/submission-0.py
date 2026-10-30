"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from functools import cmp_to_key
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        def CMP(x, y):
            if x.start > y.start:
                return 1
            elif x.start == y.start:
                if x.end > y.end:
                    return 1
                else:
                    return -1
            return -1
        if len(intervals) <= 1:
            return True
        intervals.sort(key=cmp_to_key(CMP))

        for r in range(1, len(intervals)):
            if intervals[r].start < intervals[r - 1].end:
                return False
        return True