class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        print(len(res))
        return len(res) != len(nums)