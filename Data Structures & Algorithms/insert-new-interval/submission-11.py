class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # if len(intervals) == 0:
        #     return [newInterval]

        for i in range(len(intervals)):
            if (intervals[i][0] <= newInterval[0] and newInterval[0] <= intervals[i][1]) or (intervals[i][0] <= newInterval[1] and newInterval[0] <= intervals[i][0]):
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            elif intervals[i][0] < newInterval[0]:
                res.append([intervals[i][0], intervals[i][1]])
            else:
                res.append([newInterval[0], newInterval[1]])
                newInterval[0], newInterval[1] = intervals[i][0], intervals[i][1]
        res.append([newInterval[0], newInterval[1]])
        return res

        
