class Solution:
    def numDecodings(self, s: str) -> int:
        D = {str(i - 64): chr(i) for i in range(65, 91)}
        n = len(s)
        cnt = [0] * n
        
        # initial state of index 0
        if s[0] in D:
            cnt[0] = 1

        for i in range(1, n):
            if s[i - 1: i + 1] in D:
                if i >= 2:
                    cnt[i] += cnt[i - 2]
                else:
                    cnt[i] += 1
            if s[i] in D:
                cnt[i] += cnt[i - 1]
        return cnt[n - 1]
