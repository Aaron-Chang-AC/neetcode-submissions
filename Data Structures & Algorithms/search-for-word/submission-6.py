class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.V = set([])
        self.s = []
        self.w = word
        self.b = board
        self.res = False
        def dfs(x, y, l):
            t = tuple([x, y])
            if self.res:
                return
            if self.b[x][y] == self.w[l] and t not in self.V:
                self.V.add(t)
                if l == len(self.w) - 1:
                    self.res = True
                    return
                if x > 0:
                    dfs(x - 1, y, l + 1)
                if x < len(self.b) - 1:
                    dfs(x + 1, y, l + 1)
                if y > 0:
                    dfs(x, y - 1, l + 1)
                if y < len(self.b[0]) - 1:
                    dfs(x, y + 1, l + 1)
                self.V.remove(t)
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                if self.b[i][j] == word[0]:
                    dfs(i, j, 0)
        return self.res

