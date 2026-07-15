class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        for i in range(len(s)):
            if s[i] == "*":
                starStack.append(i)
            if s[i] == "(":
                leftStack.append(i)
            if s[i] == ")":
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        while leftStack and starStack:
            if leftStack.pop() > starStack.pop():
                return False
        if leftStack:
            return False
        return True