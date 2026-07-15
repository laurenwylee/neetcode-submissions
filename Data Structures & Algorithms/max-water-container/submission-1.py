class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l = 0
        r = len(heights)-1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            m = max(area, m)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return m
