class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for i in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                u = dp[i-1][j] if i - 1 >= 0 else 0
                l = dp[i][j-1] if j - 1 >= 0 else 0
                dp[i][j] = max(u,l)

                if text1[i] == text2[j]:
                    d = dp[i-1][j-1] if i - 1 >= 0 and j - 1 >= 0 else 0
                    d += 1
                    dp[i][j] = d
        # for i in dp:
        #     print(i)
        return dp[len(text1)-1][len(text2)-1]
                
        
'''
   b  m  j  k  b  k  j  k  v
b [1, 1, 1, 1, 1, 1, 1, 1, 1]
s [1, 1, 1, 1, 1, 1, 1, 1, 1]
b [1, 1, 1, 1, 2, 2, 2, 2, 2]
i [1, 1, 1, 1, 2, 2, 2, 2, 2]
n [1, 1, 1, 1, 2, 2, 2, 2, 2]
i [1, 1, 1, 1, 2, 2, 2, 2, 2]
n [1, 1, 1, 1, 2, 2, 2, 2, 2]
m [1, 2, 2, 2, 2, 2, 2, 2, 2]

   j  m  j  k  b  k  j  k  v
b [0, 0, 0, 0, 1, 1, 1, 1, 1]
s [0, 0, 0, 0, 1, 1, 1, 1, 1]
b [0, 0, 0, 0, 1, 1, 1, 1, 1]
i [0, 0, 0, 0, 1, 1, 1, 1, 1]
n [0, 0, 0, 0, 1, 1, 1, 1, 1]
i [0, 0, 0, 0, 1, 1, 1, 1, 1]
n [0, 0, 0, 0, 1, 1, 1, 1, 1]
m [0, 1, 1, 1, 1, 1, 1, 1, 1]

'''