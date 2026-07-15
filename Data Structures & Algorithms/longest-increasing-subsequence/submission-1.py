class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        def dfs(i):
            if i == 0:
                dp[i] = 1
                return 1
            longest = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    longest = max(dfs(j) + 1, longest)
            dp[i] = longest
            return longest
        for i in range(len(nums)):
            dfs(i)
        return max(dp)