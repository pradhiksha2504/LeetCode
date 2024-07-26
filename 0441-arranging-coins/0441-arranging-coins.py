class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >0:
            if n < i:
                return i-1
            n -= i
            i +=  1
        return i -1

        