class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        D = {}
        res = 0

        # visited init to 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                D[(i,j)] = 0

        def dfs(x,y):
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[x]) - 1:
                return
            if D[(x,y)] == 1:
                return
            
            # visit = 1
            D[(x,y)] = 1

            if grid[x][y] == "1":
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and D[(i,j)] == 0:
                    res+=1
                    dfs(i,j)
                else:
                    D[(i,j)]=1
        return res