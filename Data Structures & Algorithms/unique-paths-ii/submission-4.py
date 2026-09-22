class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        d = [[0, 1], [1, 0]]
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        
        dp[0][0] = 1
        # for i in range(len(obstacleGrid)):
        #     if obstacleGrid[i][0] != 1:
        #         dp[i][0] = 1
        # for j in range(len(obstacleGrid[0])):
        #     if obstacleGrid[0][j] != 1:
        #         dp[0][j] = 1
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j]
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j-1]
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]