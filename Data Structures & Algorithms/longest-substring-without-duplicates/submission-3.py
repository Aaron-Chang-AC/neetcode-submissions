class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        D = {}
        l = 0
        r = l + 1 
        
        if len(s) <= 1:
            return len(s)
        
        D[s[l]] = 0
        while r < len(s) and l < r:
            if s[r] not in D:
                D[s[r]] = r
            else:
                t = D[s[r]]
                for j in range(l, t + 1):
                    #print(D[s[j]])
                    del D[s[j]]
                l = t + 1
                D[s[r]] = r
            r+=1
            res = max(res, len(D))
        return res