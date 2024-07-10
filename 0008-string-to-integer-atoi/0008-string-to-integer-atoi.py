import sys
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        # s = s.replace(" ","")
        if len(s)==0:
            return 0
        print(s)
        a=""
        sign = 1
        if s[0] in ["-","+"]:
            if s[0] == "-":
                sign = -1
                s = s.replace("-","",1)
            else:
                s = s.replace("+","",1)
        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                a+=s[i]
            else:
                break
        print(a)
        if len(a)!=0:
            num = sign*int(a)
            min_val = -2**31
            max_val = 2**31 - 1
            if num < min_val:
                return min_val
            elif num > max_val:
                return max_val
            else:
                return num
        return 0
        