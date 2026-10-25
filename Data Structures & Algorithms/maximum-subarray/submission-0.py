class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        s = 0
        res = -100001

        while l <= r and r < len(nums):
            s = max(s + nums[r], nums[r])
            if nums[r] < 0:
                r += 1
                l = r
            else:
                r += 1
            res = max(res, s)
        
        return res

