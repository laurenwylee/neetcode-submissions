class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)
            else:
                if len(stack) == 0 :
                    return False
                latest = stack[-1]
                if latest == "(" and x != ")":
                    return False
                if latest == "{" and x != "}":
                    return False
                if latest == "[" and x != "]":
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False