class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1
        for i in range(0, len(nums), 2):
            num, deno = nums[i], nums[i+1]
            numerator = numerator * deno + num * denominator
            denominator *= deno
        com_div = gcd(numerator, denominator)
        return f"{numerator // com_div}/{denominator // com_div}"
        