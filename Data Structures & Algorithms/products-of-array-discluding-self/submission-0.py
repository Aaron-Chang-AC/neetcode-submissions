class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)
        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            l[i] = prefix
            prefix *= nums[i]
        
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            r[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)):
            res[i] = l[i] * r[i]
        
        return res