class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        D = {0:0}
        coins.sort()
        for c in coins:
            D[c] = 1 
        for a in range(amount + 1):
            for c in coins:
                D[a + c] = min (D.get(a + c, 10001), D.get(a, 10001) + 1)

        #print(D)
        return D[amount] if (amount in D and D[amount] < 10001) else -1
'''
   1 2 5
1  1 
2  2 1
3  3 2
4  4 
5  5
6  6
7  7
8  8
9  9
10 10
11 11
'''
        