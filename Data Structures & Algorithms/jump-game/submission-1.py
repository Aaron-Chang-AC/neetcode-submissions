class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        res = False
        cur = 0

        while r < len(nums):
            if cur < r:
                return False
            cur = max(cur, r + nums[r])
            # print (cur)
            # print (r)
            # print ()
            r += 1
            

        return True if cur >= len(nums) - 1 else False