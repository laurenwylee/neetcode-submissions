class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * len(nums)
        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dfs(j))
            return dp[i]
        for i in range(n):
            dfs(i)
        return max(dp)
            