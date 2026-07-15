class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, t = stack.pop()
                ret[idx] = i - idx
            stack.append((i, temp))
        return ret