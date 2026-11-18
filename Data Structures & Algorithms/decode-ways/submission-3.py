class Solution:
    def numDecodings(self, s: str) -> int:
        D = {str(i - 64): chr(i) for i in range(65, 91)}
        V = set([])
        n = len(s)
        st = []
        cnt = [0] * n

        if n == 1:
            return int(s[0] in D)

        if s[0] in D:
            cnt[0] = 1
        if s[0: 2] in D:
            cnt[1] = 1
        if s[1] in D and s[0] in D:
            cnt[1] += 1

        for i in range(2, n):
            if i > 0 and s[i - 1: i + 1] in D:
                cnt[i] += cnt[i - 2]
            if s[i] in D:
                cnt[i] += cnt[i - 1]
        print(cnt)
        return cnt[n - 1]
    
    '''
    22 6

    2
    '''