class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited = set([])
        for i in range(n):
            adj[i] = []
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        cnt = 0
        s = []
        #print(adj)
        for j in adj:
            s = []
            if j not in visited:
                cnt += 1
                for k in adj[j]:
                    if k not in visited:
                        s.append(k)
                while s:
                    t = s.pop()
                    visited.add(t)
                    for m in adj[t]:
                        if m not in visited:
                            s.append(m)
        return cnt
