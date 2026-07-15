class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            if not stack:
                stack.append((height, i))
                continue
            idx = i
            while stack and stack[-1][0] > height:
                h, idx = stack.pop()
                area = (i - idx) * h
                max_area = max(area, max_area)
            stack.append((height, idx))
        while stack:
            h, idx = stack.pop()
            area = (len(heights) - idx) * h
            max_area = max(area, max_area)
        return max_area