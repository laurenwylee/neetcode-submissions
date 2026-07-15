class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = r+ 1
            else:
                m = max(prices[r] - prices[l], m)
                r += 1
        return m