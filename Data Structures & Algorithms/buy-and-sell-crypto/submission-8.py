class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l = 0
        r = 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxprofit = max(profit, maxprofit)
            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1
        return maxprofit