class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        longestPath = 0
        dp = [[-1] * m for _ in range(n)]
        d = [[1, 0], [-1, -0], [0, 1], [0,-1]]
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            maxLength = 0
            for dx, dy in d:
                if i + dx < 0 or i + dx >= n or j + dy < 0 or j + dy >= m:
                    continue
                if matrix[i+dx][j + dy] <= matrix[i][j]:
                    continue
                maxLength = max(dfs(i + dx, j + dy), maxLength) 
            dp[i][j] = 1 + maxLength
            return dp[i][j]
                    
        for i in range(n):
            for j in range(m):
                longestPath = max(longestPath, dfs(i, j))
        return longestPath