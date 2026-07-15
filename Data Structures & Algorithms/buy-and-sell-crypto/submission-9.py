class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best  = 0
        l = 0
        r = l + 1
        while r < len(prices):
            best = max(prices[r] - prices[l], best)
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r+=1
        return best
