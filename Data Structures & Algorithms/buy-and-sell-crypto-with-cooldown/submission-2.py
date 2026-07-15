class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[None] * 2 for _ in range(len(prices) + 1)]
        def dfs(i, own):
            if i >= len(prices):
                return 0
            if dp[i][own]:
                return dp[i][own]
            if own:
                # either sell or don't sell
                dp[i][own] = max(prices[i] + dfs(i +  2, not own), dfs(i + 1, own))
            else:
                dp[i][own] = max(-prices[i] + dfs(i + 1, not own), dfs(i + 1, own))
            return dp[i][own]
        dfs(0, False)
        return dp[0][False]
            