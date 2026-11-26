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
'''
the dp stores the LIS in position i
loop over nums, if nums[i] > nums[j] (j is any element before index i)
then dp[i] is the maximal LIS + 1 in range i~0 which is j
'''