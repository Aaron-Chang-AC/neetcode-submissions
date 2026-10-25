class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 31
        while n > 0:
            res = res | ((n & 1) << i)
            i -= 1
            n >>= 1
        return res
