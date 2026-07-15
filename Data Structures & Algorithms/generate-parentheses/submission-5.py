class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(opened, closed, curr):
            if opened == closed and opened + closed == 2 * n:
                ret.append(curr)
                return 
            if opened > n or closed > n:
                return
            if closed < opened:
                curr = curr + ")"
                dfs(opened, closed + 1, curr)
                curr = curr[:-1]
            if opened < n:
                curr = curr + "("
                dfs(opened + 1, closed, curr)
                curr = curr[:-1]
        dfs(0, 0, "")
        return ret
            


