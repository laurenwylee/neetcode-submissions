class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        def dfs(i):
            if i == 0:
                dp[0] = nums[i]
                return nums[i]
            dp[i] = max(dfs(i - 1) + nums[i], nums[i])
            return dp[i]
        dfs(len(nums) - 1)
        return max(dp)