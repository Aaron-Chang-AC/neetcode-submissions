class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range (0 , n + 1):
            t = i
            c = 0
            while t > 0:
                t = t & (t - 1)
                c += 1
            res = res + [c]

        return res