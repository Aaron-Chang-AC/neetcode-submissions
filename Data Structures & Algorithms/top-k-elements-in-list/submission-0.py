class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D={}
        res=[]
        for i in nums:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        D = {k_t : v_t for k_t, v_t in sorted(D.items(), key = lambda item: item[1], reverse=True)}
        
        for i in D:
            if k > 0:
                res = res + [i]
                k -= 1
            else:
                break
        return res