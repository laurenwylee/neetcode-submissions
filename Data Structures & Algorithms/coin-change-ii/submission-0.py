class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        def dfs(i, target):
            if target == 0:
                return 1
            if i >= len(coins) or target < 0:
                return 0
            if dp[i][target] != - 1:
                return dp[i][target]
            dp[i][target] = dfs(i+1, target) + dfs(i, target - coins[i])
            return dp[i][target]
        return dfs(0, amount)