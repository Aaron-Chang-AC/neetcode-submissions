class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        D = set(wordDict)
        V = set([])
        n = len(s)
        st = []

        for i in range(n):
            if s[0:i + 1] in D:
                if i == n - 1:
                    return True
                st.append(i)

        while st:
            t = st.pop()
            if t in V:
                continue
            V.add(t)
            #print(t)
            for i in range(t + 1, n):
                j = s[t + 1:i + 1]
                if j in D:
                    if i == n - 1:
                        return True
                    if i not in V:
                        st.append(i)

        return False
'''
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        D = set(wordDict)
        V = set([])
        n = len(s)
        st = []

        for i in range(n):
            if s[0:i + 1] in D:
                if i == n - 1:
                    return True
                st.append(tuple([0, i]))

        while st:
            t = st.pop()
            if t in V:
                continue
            V.add(t)
            #print(t)
            for i in range(t[1] + 1, n):
                j = s[t[1] + 1:i + 1]
                if j in D:
                    if i == n - 1:
                        return True
                    if tuple([t[1] + 1, i]) not in V:
                        st.append(tuple([t[1] + 1, i]))

        return False

DFS:
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

DP:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        D = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in D:
                    dp[i] = True
                    break

        return dp[n]
'''