class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        res = (a ^ b) & MASK
        carry = (a & b & MASK) << 1

        while carry != 0:
            temp = res
            res = (temp ^ carry) & MASK
            carry = (temp & carry) & MASK
            carry = (carry << 1) & MASK
        return ~(res ^ MASK) if res > 0x7FFFFFFF else res
            
