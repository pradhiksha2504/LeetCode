class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        n = len(digits)
        tens = pow(10,n-1)
        integer = 1
        for i in range(n):
            integer += (digits[i]*tens)
            tens //=10
        res = []
        while integer > 0:
            rem = integer % 10
            res.append(rem)
            integer //= 10

        return res[::-1]
        