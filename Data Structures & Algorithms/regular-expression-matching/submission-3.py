class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if i < len(s) and dp[i][j] != None:
                return dp[i][j]
            match = False
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                match = True
            if j < (len(p) - 1) and p[j + 1] == "*":
                dp[i][j] = (match  and dfs(i + 1,j)) or dfs(i, j + 2)
                return dp[i][j]
            if match:
                dp[i][j] = dfs(i + 1, j + 1)
                return dp[i][j]
            if not match:
                dp[i][j] = False
                return False
        return dfs(0, 0)
            