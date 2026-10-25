class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_t = ""
        for i in s:
            if ord(i) <= ord('z') and ord(i) >= ord('a'):
                s_t += chr(ord(i) - 32)
            elif ord(i) <= ord('Z') and ord(i) >= ord('A'):
                s_t += i
            elif ord(i) <= ord('9') and ord(i) >= ord('0'):
                s_t += i
        #print(s_t)
        if len(s_t) <= 1:
            return True
        
        l = 0
        r = len(s_t) - 1

        while l < r:
            if s_t[l] != s_t[r]:
                return False
            else:
                l+=1
                r-=1
        return True
