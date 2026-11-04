class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        r = 0
        D = {}
        while r < len(s):
            D[s[r]] = D.get(s[r], 0) + 1
            if (r - l + 1) - max(D.values()) < k:
                res = max(res, r - l + 1)
            else:
                while (r - l + 1) - max(D.values()) > k:
                    D[s[l]] -= 1
                    l += 1
                res = max(res, r - l + 1)
            r += 1
        return res
'''
xyzyxxx k=2
l

'''


            