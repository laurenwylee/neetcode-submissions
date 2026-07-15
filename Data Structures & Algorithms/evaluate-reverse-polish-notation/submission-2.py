class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x != "+" and x != "-" and x != "*" and x != "/":
                stack.append(x)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if x == "+":
                    stack.append(a+b)
                elif x == "-":
                    stack.append(b-a)
                elif x == "*":
                    stack.append(a*b)
                elif x == "/":
                    stack.append(int(b/a))
        return int(stack.pop())