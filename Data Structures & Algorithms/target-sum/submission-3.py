class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        low = 0
        high = 0
        for n in nums:
            low -= n
            high += n
        dp = [[-1] * (abs(low) + abs(high) + 1) for _ in range(len(nums))]
        def dfs(i, targ):
            if i >= len(nums) and targ == target:
                return 1
            if i >= len(nums):
                return 0
            if dp[i][targ] != -1:
                return dp[i][targ]
            return dfs(i + 1, targ - nums[i]) + dfs(i + 1, targ + nums[i])

        return dfs(0, 0)