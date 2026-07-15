class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r 
                r = r + 1
            else:
                maximum = max(prices[r] - prices[l], maximum)
                r += 1
        return maximum