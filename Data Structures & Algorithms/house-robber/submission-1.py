class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        D = {i: 0 for i in range(n)}
        for i in range(n):
            D[i] = D[i] + nums[i]
            for j in range(i + 2, n):
                D[j] = max(D[j], D[i])
        return max(D.values())

'''
D = {
0: 0 (idx map to values)
1: 0
...
}

'''