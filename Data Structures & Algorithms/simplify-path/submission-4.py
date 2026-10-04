class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        l = 0
        r = l+1
        while r < len(path) and path[r] != "/":
            r += 1
        print(path[l + 1: r])
        while r < len(path):
            if r - l == 1:
                while r < len(path) and path[r] == "/":
                    l = r
                    r += 1
            else:
                directory = path[l + 1: r]
                if directory == "..":
                    if stack:
                        stack.pop()
                elif directory != ".":
                    stack.append(directory)
                l = r
                r += 1
            while r < len(path) and path[r] != "/":
                r += 1
        directory = path[l + 1:r]
        if directory == "..":
            if stack:
                stack.pop()
        elif directory != "." and path[r - 1] != "/":
            stack.append(directory)
        if not stack:
            return "/"
        return "/" + "/".join(stack)
            