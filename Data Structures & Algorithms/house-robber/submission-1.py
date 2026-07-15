class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums)
        dp[len(nums) - 1] = nums[len(nums) - 1]
        dp[len(nums) - 2] = nums[len(nums) - 2]
        for x in range(len(nums) - 3, -1, -1 ):
            dp[x] = max(dp[x+1], nums[x] + dp[x+2])
        return max(dp[0], dp[1])
        