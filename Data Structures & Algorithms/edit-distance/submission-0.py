class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # n is col and m is row
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        def dfs(i, j):
            if j == n:
                dp[i][j] = m - i
                return dp[i][j]
            if i == m: 
                dp[i][j] = n - j
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = dfs(i+1, j + 1)
            else:
                interm = min(dfs(i + 1, j), dfs(i, j + 1))
                interm = min(interm, dfs(i + 1, j + 1))
                dp[i][j] = 1 + interm
            return dp[i][j]
        return dfs(0, 0)
       