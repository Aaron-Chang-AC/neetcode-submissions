class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        s = 0 # current sum
        res = -100001

        while r < len(nums):
            s = max(s + nums[r], nums[r])
            r += 1
            res = max(res, s)
            #print (f"s: {s}, res: {res}")
        
        return res

