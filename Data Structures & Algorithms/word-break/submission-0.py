class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.S = s
        self.D = set(wordDict)
        self.V = set([])
        self.res = False
        self.n = len(s)

        def helper(l, r):
            if self.res or r > self.n - 1 or tuple([l, r]) in self.V:
                return
            self.V.add(tuple([l, r]))
            if self.S[l:r + 1] in self.D:
                if r == self.n - 1:
                    self.res = True
                else:
                    helper(r + 1, r + 1)
            helper(l, r + 1)
        
        helper(0, 0)
        return self.res
        