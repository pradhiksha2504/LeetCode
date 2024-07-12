class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        n = len(mountain)
        l,r = 1,2
        while l < n and r < n:
            if mountain[l] > mountain[r] and mountain[l]  > mountain[l-1]:
                res.append(l)
            l += 1
            r += 1
        return res
