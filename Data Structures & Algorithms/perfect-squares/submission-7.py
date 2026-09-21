class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 0
            while j * j <= i:
                dp[i] = min(1 + dp[i - (j * j)], dp[i])
                j += 1
        return dp[n]