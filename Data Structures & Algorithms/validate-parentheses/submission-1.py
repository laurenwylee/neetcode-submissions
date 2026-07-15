class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)
            else:
                if stack == []:
                    return False
                if x == ")":
                    res = stack.pop()
                    if res != "(":
                        return False
                if x == "}":
                    res = stack.pop()
                    if res != "{":
                        return False
                if x == "]":
                    res = stack.pop()
                    if res != "[":
                        return False
                
        if stack != []:
            return False
        return True

        
        