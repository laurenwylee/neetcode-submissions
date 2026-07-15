class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = []
        star = []
        for i in range(len(s)):
            if s[i] == "(":
                opened.append(i)
                continue
            if s[i] == "*":
                star.append(i)
                continue
            if s[i] == ")" and opened:
                opened.pop()
            elif s[i] == ")" and star:
                star.pop()
            else:
                return False
        if len(opened) > len(star):
            return False
        while opened:
            o = opened.pop()
            s = star.pop()
            if o > s:
                return False
        return True