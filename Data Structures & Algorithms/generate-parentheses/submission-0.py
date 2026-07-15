class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        def backtrack(openn, closen):
            if openn == closen == n:
                res.append("".join(s))
            if openn < n:
                s.append("(")
                backtrack(openn+1, closen)
                s.pop()
            if closen < openn:
                s.append(")")
                backtrack(openn, closen+1)
                s.pop()
        backtrack(0, 0)
        return res

