class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        m = 0
        # heights.append(0)
        for i in range(len(heights)):
            if stack == []:
                stack.append(i)
            else:
                if heights[stack[-1]] <= heights[i]:
                    stack.append(i)
                else:
                    while stack != [] and heights[stack[-1]] > heights[i]:
                        idx = stack.pop()
                        if stack != []:
                            x = stack[-1]
                        else:
                            x = -1  
                        m = max((i - x - 1) * (heights[idx]), m)
                    stack.append(i)
        while stack:
            idx = stack.pop()
            if stack != []:
                x = stack[-1]
            else:
                x = -1   
            m = max(m, heights[idx] * (len(heights) - x - 1))
        return m
