class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = 0
        r = len(nums) - 1
        #print(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r and l >= 0:
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                if nums[l] + nums[r] < -nums[i]:
                    l+=1
                else:
                    r-=1
        D = {}
        for i in res:
            D[tuple(i)] = 1

        return [list(i) for i in D.keys()]
