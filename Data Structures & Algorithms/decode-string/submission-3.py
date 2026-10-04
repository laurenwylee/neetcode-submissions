class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        stack = []
        l = 0
        r = 0
        while r < len(s):
            if s[r].isalpha():
                res.append(s[r])
            elif s[r].isdigit():
                while r < len(s) and s[r].isdigit():
                    r += 1
                stack.append(s[r])
                num = int(s[l:r])
                print(num)
                l = r
                while r < len(s) and stack:
                    r += 1
                    if s[r] == "[":
                        stack.append(s[r])
                    if s[r] == "]":
                        stack.pop()
                inner = s[l+1:r]
                print(inner)
                res.append(num * self.decodeString(inner))
            r += 1
            l = r
        print(res)
        return "".join(res)