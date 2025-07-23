class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumval = 0
        productval = 1
        n1 = n
        while n1 > 0:
            rem = n1 % 10
            sumval += rem
            productval *= rem
            n1 //= 10
        if n % (sumval + productval) == 0:
            return True
        return False
        