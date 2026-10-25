class Solution:

    def encode(self, strs: List[str]) -> str:
        pre = '#w@!'
        res = ''
        for i in strs:
            res += pre + i
        #print(res)
        return res
    def decode(self, s: str) -> List[str]:
        s_t = s
        L = s.split('#w@!')
        #print(L)
        return L[1:]