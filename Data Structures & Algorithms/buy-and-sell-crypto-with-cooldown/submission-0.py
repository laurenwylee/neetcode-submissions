class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices))]
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            # bought
            if buy == 1:
                # if sell tomorrow
                profit = dfs(i+1, 0) - prices[i]
                # or keep for another day
                dp[i][buy] = max(profit, dfs(i+1, buy))
            # sell
            else:
                dp[i][buy] = max(prices[i] + dfs(i+2, 1), dfs(i+1, buy))
            return dp[i][buy]
        return dfs(0, 1)
        