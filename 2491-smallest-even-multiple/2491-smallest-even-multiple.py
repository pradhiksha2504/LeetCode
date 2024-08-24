class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 2
        while i % n != 0:
            i += 2
        return i
        