class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return n
        val = 1
        for i in range(n):
            val += (i*4)
            # print(val)
        return val
        