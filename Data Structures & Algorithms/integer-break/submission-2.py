class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            maximum = -1
            for j in range(1, i):
                if dp[i - j] == -1:
                    dp[i - j] = dfs(i - j)
                maximum = max(maximum, j * dp[i - j], j * (i - j))
            dp[i] = maximum
            return maximum

        return dfs(n)
            