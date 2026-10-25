class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 101
        r = -1
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i+1]:
                l , r = min(prices[i], l) , max(prices[i+1], r) 
                res = max(res, r - l)
            else:
                r = -1 # reset r only
        return res