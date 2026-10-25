class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        D = {}
        res = 0
        for i in nums:
            D[i] = 1
        
        for i in nums:
            if i - 1 not in D:
                t = 1
                j = i
                while j + 1 in D:
                    t += 1
                    j += 1
                res = max(res, t)
        return res


