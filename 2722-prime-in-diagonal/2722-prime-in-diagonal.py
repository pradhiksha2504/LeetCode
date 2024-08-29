class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(n):
            if n < 2:
                return False
            up = int(n**0.5)
            for i in range(2, up+1):
                if n % i == 0:
                    return False
            else:
                return True
            return False

        n = len(nums)
        diagonals = [nums[i][i] for i in range(n)]
        for i in range(n):
            diagonals.append(nums[i][(n-i-1)])

        maxi = 0
        for i in diagonals:
            if prime(i):
                maxi = max(i, maxi)

        return maxi


        