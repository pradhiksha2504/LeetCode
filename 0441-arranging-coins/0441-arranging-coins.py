class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        i = 1
        while n >0:
            n -= i
            i +=  1
            row += 1
        if n < 0:
            return row-1
        return row

        