class Solution:
    def reverse(self, x: int) -> int:
        M = 2 ** 31 - 1
        m = -(2 ** 31)
        t = 0
        sign = -1 if x < 0 else 1
        x_t = x // sign
        
        while x_t > 0:
            if sign > 0 and (t > M // 10 or (t == M // 10 and x_t % 10 > M % 10)):
                return 0
            if sign < 0 and (t > M // 10 or (t == M // 10 and x_t % 10 > (M % 10) + 1)):
                return 0
            t = t * 10 + (x_t % 10)
            x_t = x_t // 10
        return sign * t
