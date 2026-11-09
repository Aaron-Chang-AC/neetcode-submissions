class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        D = {0:0}
        coins.sort()
        for c in coins:
            D[c] = 1 
        for a in range(amount + 1):
            for c in coins:
                if a in D and a + c <= amount:
                    # bottom up DP
                    D[a + c] = min (D.get(a + c, 10001), D.get(a, 10001) + 1)

        #print(D)
        return D[amount] if (amount in D and D[amount] < 10001) else -1
        