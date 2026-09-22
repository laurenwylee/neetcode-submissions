class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        def dfs(total):
            if dp[total] != 0:
                return dp[total]
            for n in nums:
                if n > total:
                    continue
                dp[total] += dfs(total - n)
            return dp[total]
        return dfs(target)
            

