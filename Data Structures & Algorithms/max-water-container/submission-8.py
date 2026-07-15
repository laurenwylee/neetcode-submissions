class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maximum_amt = -1
        while l != r:
            maximum_amt = max(maximum_amt, (r-l) * min(heights[r], heights[l]))
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        return maximum_amt