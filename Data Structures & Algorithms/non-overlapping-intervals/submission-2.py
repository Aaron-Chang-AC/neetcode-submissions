from functools import cmp_to_key
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        n = len(intervals)
        
        def CMP(x,y):
            if x[0] > y[0]:
                return 1
            elif x[0] == y[0] and x[1] > y[1]:
                return 1
            return -1
        intervals.sort(key = cmp_to_key(CMP))
        #print(intervals)
        mg_i = intervals[0]
        for i in range(1, n):
            if mg_i[1] <= intervals[i][0]:
                mg_i[1] = intervals[i][1]
            else:
                mg_i[1] = min(mg_i[1], intervals[i][1])
                res += 1
        #print(res)
        return res