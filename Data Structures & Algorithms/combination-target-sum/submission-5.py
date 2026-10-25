class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        D = {}
        nums.sort()

        for i in range(0, target + 1):
            D[i] = []

        for n in nums:
            for i in range(n, target + 1):
                if i == n:
                    D[i].append([n])
                for j in D[i - n]:
                    D[i].append(j.copy() + [n])

        #print(D)
        return D[target]
