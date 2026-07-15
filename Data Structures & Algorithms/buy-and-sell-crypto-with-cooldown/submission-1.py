class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[None] * 2 for _ in range(len(prices))]
        def dfs(i, own):
            if i >= len(prices):
                return 0
            if dp[i][own] != None:
                return dp[i][own]
            # if i own coin, either a sell, or a keep 
            if own:
                dp[i][own] = max(prices[i] + dfs(i + 2, not own), dfs(i + 1, own))
            # if i dont own, either buy or dont buy
            else:
                dp[i][own] = max(-prices[i] + dfs(i + 1, not own), dfs(i+1, own))
            return dp[i][own]
        return dfs(0, False)