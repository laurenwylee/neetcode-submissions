class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x != "+" and x != "-" and x != "/" and x != "*":
                stack.append(int(x))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if x == "+":
                    stack.append(op1 + op2)
                if x == "-":
                    stack.append(op2 - op1)
                if x == "*":
                    stack.append(op1 * op2)
                if x == "/":
                    stack.append(int(op2 / op1))
        return stack.pop()
                
