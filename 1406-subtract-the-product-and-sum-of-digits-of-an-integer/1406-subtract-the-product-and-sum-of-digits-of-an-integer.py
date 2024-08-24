class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total=0
        product = 1
        while n > 0:
            rem = n % 10
            total+=rem
            product *= rem
            n //= 10
        return product - total
        