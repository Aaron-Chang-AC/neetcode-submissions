class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = [''.join(sorted(n)) for n in strs]
        D = {}
        res = []
        for i, n in enumerate(s):
            if n not in D:
                D[n] = []
            D[n].append(strs[i])
        for k in D:
            res.append(D[k])
        return res

'''
'''