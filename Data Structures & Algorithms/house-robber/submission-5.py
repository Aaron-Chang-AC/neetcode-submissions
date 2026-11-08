class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        r2, r1 = 0, 0
        res = max(r1, r2)
        for i in range(n):
            res = max(r2 + nums[i], r1)
            r2 = r1
            r1 = res
        return res
'''
optimal solution:
now: r2 r1 n n+1
next: x  r2 r1 n

Other array based solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = [0] * n
        for i in range(n):
            res[i] = max(res[i - 2] + nums[i], res[i - 1])
        return max(res)

for each step -> maximum is the step from res[i - 2] plus nums[i]
, or use res[i - 1] indicating not to rob nums[i]

'''