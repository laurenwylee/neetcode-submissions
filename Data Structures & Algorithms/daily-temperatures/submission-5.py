class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if stack:
                (top, idx) = stack[len(stack) - 1]
                while stack and t > top:
                    stack.pop()
                    ret[idx] = i - idx
                    if stack:
                        (top, idx) = stack[len(stack) - 1]
            stack.append((t, i))
        return ret
