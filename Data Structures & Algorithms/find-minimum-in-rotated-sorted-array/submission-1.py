class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[len(nums) - 1] > nums[0]:
            return nums[0]
        f = False
        l = 0
        r = len(nums) - 1
        mid = (r + l) // 2

        while l < r:
            if mid == l:
                return nums[mid + 1] if nums[mid] > nums[r] else nums[r]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[l] < nums[mid]:
                l = mid
            else:
                r = mid
            mid = (r + l) // 2
        return nums[mid + 1]