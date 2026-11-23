import heapq as hq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = Counter(nums)
        h = [[-D[k], k] for k in D]
        hq.heapify(h)
        return [hq.heappop(h)[1] for i in range(k)]
# from functools import cmp_to_key
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # D=Counter(nums)
        # def CMP(x,y):
        #     if x[1] < y[1]:
        #         return 1
        #     else:
        #         return -1
        # temp = sorted(D.items(), key=cmp_to_key(CMP))

        # return [temp.pop(0)[0] for i in range(k)]