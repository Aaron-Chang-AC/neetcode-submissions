class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = [''.join(sorted(i)) for i in strs]
        D = {}
        for i in range(0 , len(strs)):
            if strs_sorted[i] not in D:
                D[strs_sorted[i]] = []
            D[strs_sorted[i]].append(strs[i])
        
        return [D[i] for i in D.keys()]