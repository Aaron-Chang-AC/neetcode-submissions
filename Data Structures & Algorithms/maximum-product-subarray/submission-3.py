class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_v = 1
        max_v = 1
        res = -20001

        

        for i in nums:
            min_v_t = min (min_v * i, max_v * i, i)
            max_v_t = max (min_v * i, max_v * i, i)

            # print(min_v_t)
            # print(max_v_t)

            min_v, max_v = min_v_t, max_v_t
            res = max(res, max_v)
        
        return res
            
'''
find min and max in for each number in nums
2     4         -3       5      -2
0,2   0, 8 -24, -3 -120, 5 -2, 240
'''