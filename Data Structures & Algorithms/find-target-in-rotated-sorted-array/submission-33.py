class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums):
            if len(nums) == 1 or nums[len(nums) - 1] > nums[0]:
                return 0, nums[0]

            l = 0
            r = len(nums) - 1
            mid = (r + l) // 2

            while l < r:
                if mid == l:
                    if nums[mid] > nums[r]:
                        return mid + 1, nums[mid + 1]
                    else:
                        return r, nums[r]
                elif nums[mid] > nums[mid + 1]:
                    return mid + 1, nums[mid + 1]
                elif nums[l] < nums[mid]:
                    l = mid
                else:
                    r = mid
                mid = (r + l) // 2
            return mid + 1, nums[mid + 1]

        def findTar(nums, tar):
            if len(nums) == 1:
                return 0 if nums[0] == tar else -1
            l = 0
            r = len(nums) - 1
            m = (l + r) // 2
            while l <= r:
                m = (l + r) // 2
                if nums[m] == tar:
                    return m
                if nums[m] < tar:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        l = 0
        r = len(nums) - 1
        i, piv = findMin(nums)
        print((i, piv))

        if i == 0:
            return findTar(nums, target)
        if target == nums[i]:
            return i
        if nums[r] < target:
            return findTar(nums[:i], target)
        ans = findTar(nums[i:], target)
        return i + ans if ans != -1 else -1

        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] == target:
        #         return m
        #     if nums[l] <= nums[m]:
        #         if nums[l] <= target < nums[m]:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     else:
        #         if nums[m] < target <= nums[r]:
        #             l = m + 1
        #         else:
        #             r = m - 1
        # print(nums[l])
        # print(nums[r])
        # return -1



'''
3 4 5 6 1 2
l   m     r



'''