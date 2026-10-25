class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        m = max(nums)
        if m == len(nums) - 1:
            return m + 1
        for i in range(0, m + 1):
            res += i
        for j in nums:
            res -= j
        return res