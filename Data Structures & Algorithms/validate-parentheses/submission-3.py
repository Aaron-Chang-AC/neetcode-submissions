class Solution:
    def isValid(self, s: str) -> bool:
        L = [i for i in s]
        S = []
        res = True
        while len(L) > 0:
            t = L.pop(0)
            if t == '(' or t == '{' or t == '[':
                S.append(t)
            else:
                if len(S) > 0:
                    t2 = S.pop()
                    if (t2 == '(' and t == ')') or (t2 == '{' and t == '}') or (t2 == '[' and t == ']'):
                        continue
                    else:
                        res = False
                        break
                else:
                    res = False
                    break
        return res if len(S) == 0 else False