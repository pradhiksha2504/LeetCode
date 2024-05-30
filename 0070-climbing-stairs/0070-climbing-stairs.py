class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        for i in range(n, -1, -1):
            if i in (n, n-1):
                dp[i] = 1
            else:
                dp[i] = dp[i+1]+dp[i+2]
        print(dp)
        return dp[0]

        