class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res, part = [], []
        n = len(s)
        def dfs(i):
            if i >= n:
                res.append(part.copy())
                return
            for j in range(i, n):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
            # return res
        dfs(0)        
        return res