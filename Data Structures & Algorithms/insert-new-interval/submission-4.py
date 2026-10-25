class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if len(intervals) == 0:
            return [newInterval]
        for i, n in enumerate(intervals):
            if n[0] > newInterval[0]:
                intervals.insert(i, newInterval)
                newInterval = []
                break
            elif n[0] == newInterval[0]:
                j = i
                while j < len(intervals) - 1 and intervals[j][0] == newInterval[0] and intervals[j][1] < newInterval[1]:
                    j += 1
                intervals.insert(j, newInterval)
                newInterval = []
                break
        if len(newInterval) > 0:
            intervals.append(newInterval)
        #print(intervals)

        cur_l = intervals[0][0]
        cur_r = intervals[0][1]
        for i in range(len(intervals)):
            if cur_l <= intervals[i][0] and intervals[i][0] <= cur_r:
                cur_l = min(cur_l, intervals[i][0])
                cur_r = max(cur_r, intervals[i][1])
            else:
                res.append([cur_l, cur_r])
                cur_l, cur_r = intervals[i][0], intervals[i][1]
        res.append([cur_l, cur_r])
        return res

        
