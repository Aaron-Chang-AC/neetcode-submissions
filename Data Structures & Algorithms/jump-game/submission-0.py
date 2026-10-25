class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        r = 0
        dp[0] = True

        while r < len(nums):
            if nums[r] > 0 and dp[r]:
                for j in range(r, r + nums[r]):
                    if j + 1 < len(nums):
                        dp[j + 1] = True
            r += 1
        #print(dp)
        return dp[len(nums) - 1]