class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.res = []
        def dfs(cur, tar):
            if not tar:
                self.res.append(cur.copy())
                return
            for i in range(len(tar)):
                t = tar.pop(i)
                cur.append(t)
                dfs(cur, tar)
                tar.insert(i, t)
                cur.pop()
        dfs([], nums)
        return self.res
        