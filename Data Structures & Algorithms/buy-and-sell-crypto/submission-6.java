class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int l = 0;
        int r = 1;
        while(r < prices.length)
        {
            max = Math.max(max, prices[r] - prices[l]);
            if(prices[l] > prices[r])
            {
                l = r;
            }
            r += 1;
        }
        return max;
    }
}
