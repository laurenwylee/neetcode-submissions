class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if height[l] < min(maxLeft, maxRight):
                area = area + (min(maxLeft, maxRight) - height[l])
            if height[r] < min(maxLeft, maxRight):
                area = area + (min(maxLeft, maxRight) - height[r])
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return area
