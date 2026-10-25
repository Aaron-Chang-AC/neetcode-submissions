from functools import cmp_to_key
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
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
        for i in range(n):
            if mg_i[1] >= intervals[i][0]:
                mg_i[0] = min(mg_i[0], intervals[i][1])
                mg_i[1] = max(mg_i[1], intervals[i][1])
            else:
                res.append(mg_i)
                mg_i = intervals[i]
        res.append(mg_i)
        #print(res)
        return res
