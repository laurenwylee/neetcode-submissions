class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0,1], [1,0]]
        dp = [[-1] * n for _ in range(m)]
        def dfs(x, y):
            if x == m-1 and y == n-1:
                dp[x][y] = 1
                return 1
            if dp[x][y] != -1:
                return dp[x][y] 
            s = 0
            for dx, dy in d:
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n:
                    s += dfs(x + dx, y + dy)
            dp[x][y] = s
            return s
        dfs(0, 0)
        return dp[0][0]