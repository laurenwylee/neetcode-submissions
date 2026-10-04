class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        count = 0
        for x in operations:
            if x == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif x == "C":
                stack.pop()
            elif x == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(x))
        return sum(stack)