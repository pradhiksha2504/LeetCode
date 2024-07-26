class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        l = 0
        r = 0
        g.sort()
        s.sort()
        while l<len(g) and r<len(s):
            if g[l] <= s[r]:
                count += 1
                l += 1
            r += 1
        return count
        