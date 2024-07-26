class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        i = 1
        while n >0:
            if n < i:
                return row
            n -= i
            i +=  1
            row += 1
        return row

        