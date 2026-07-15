class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        def dfs(i , j):
            if j < i:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dfs(i, k) + dfs(k, j) + (nums[i] * nums[k] * nums[j]))
            return dp[i][j]
        return dfs(0, len(nums) -1)