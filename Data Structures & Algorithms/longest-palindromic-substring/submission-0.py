class Solution:
    def longestPalindrome(self, s: str) -> str:
        l , r = 0, 0
        n = len(s)
        res = ""
        for i in range(n):
            l , r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                t = s[l:r+1]
                if len(t) >= len(res):
                    res = t
                l -= 1
                r += 1
        
        for i in range(n - 1):
            l , r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                t = s[l:r+1]
                if len(t) >= len(res):
                    res = t
                l -= 1
                r += 1
        return res
