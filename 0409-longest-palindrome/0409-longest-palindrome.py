class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        f = {}
        for i in s:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        if len(f) == 1:
            return f[i]
        count = 0
        odd = 0
        for j in f.values():
            if j % 2 != 0:
                count += j-1
                odd += 1
            else:
                count += j
        if odd == 0:
            return count 
        return count + 1




        return count 

