class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        m = len(nums)
        dp = [1] * m
        for i in range(m):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #print(dp)
        return max(dp)
