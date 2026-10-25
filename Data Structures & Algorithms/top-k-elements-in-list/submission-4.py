from functools import cmp_to_key
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D=Counter(nums)
        res=[]
        def CMP(x,y):
            if x[1] < y[1]:
                return 1
            else:
                return -1
        temp = sorted(D.items(), key=cmp_to_key(CMP))

        for i in range(k):
            res.append(temp[i][0])
        return res

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         D={}
#         res=[]
#         for i in nums:
#             if i in D:
#                 D[i] += 1
#             else:
#                 D[i] = 1
#         D = {k_t : v_t for k_t, v_t in sorted(D.items(), key = lambda item: item[1], reverse=True)}
        
#         res = list(D.keys())[0:k]

#         return res