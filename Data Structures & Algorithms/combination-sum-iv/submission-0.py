class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        cache = {}
        def dfs(total):
            if total in cache:
                return cache[total]
            if total == 0:
                return 1
            res = 0
            for i in range(len(nums)):
                if total - nums[i] < 0:
                    break
                res += dfs(total - nums[i])
            cache[total] = res
            return res
        return dfs(target)