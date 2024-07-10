class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] in ("-","+"):
            if s[0] == "-":
                sign = -1
            s = s[1:]
        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break
        if not s:
            return 0
        num = sign*int(s)
        min_val = -2**31
        max_val = 2**31 - 1
        if num < min_val:
            return min_val
        elif num > max_val:
            return max_val
        return num
        