class Solution:
    def countSubstrings(self, s: str) -> int:
        l , r = 0, 0
        n = len(s)
        res = 0
        for i in range(n):
            l , r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        for i in range(n - 1):
            l , r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
