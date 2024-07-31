class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n%2 == 0:
            n //=2
        try:
            while n!= 1:
                if n % 3 == 0:
                    n //= 3
                elif n % 5 == 0:
                    n //= 5
                else:
                    break
        except:
            return False
        if n == 1:
            return True