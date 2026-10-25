class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        res = []
        for i, n in enumerate(nums):
            D[n] = i
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in D and D[tar] != i:
                res = [min(D[tar], i), max(D[tar], i)]
        return res
