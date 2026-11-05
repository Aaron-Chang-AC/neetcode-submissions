class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D = {i: [] for i in range(numCourses)}
        v = {i: 0 for i in range(numCourses)}
        self.res = True

        for e in prerequisites:
            D[e[0]].append(e[1])
        
        #print(D)

        def dfs(c):
            if v[c] == 1:
                self.res = False
                return
            if v[c] == 2:
                return
            v[c] = 1

            #print()
            #print(c)
            #print(v)

            for i in D[c]:
                #print(i)
                dfs(i)
            v[c] = 2 # 2 means finishing traversal
            return
        
        for i in range(numCourses):
            if v[i] != 2:
                dfs(i)
        return self.res
            
        

'''
D = {
 0: [1]
}

'''