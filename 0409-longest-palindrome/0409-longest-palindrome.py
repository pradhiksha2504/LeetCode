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
        count = 0
        odd = {}
        for i, j in f.items():
            if j % 2 != 0:
                odd.update({i:j})
            else:
                count += j
        if len(odd) > 0:
            maxifreq = max(odd.values())
            count += maxifreq
            flag = False
            for j in odd.values():
                if j == maxifreq:
                    if not flag:
                        flag = True
                        continue
                count = count + j -1
        return count




        return count 

