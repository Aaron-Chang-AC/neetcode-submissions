class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        res1 = [0] * n
        for i in range(n - 1):
            res1[i] = max(res1[i - 2] + nums[i], res1[i - 1])
        
        res2 = [0] * n
        for i in range(1, n):
            res2[i] = max(res2[i - 2] + nums[i], res2[i - 1])

        return max(max(res1), max(res2))