class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(subset, used):
            if len(subset) == len(nums):
                ret.append(subset.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    subset.append(nums[i])
                    dfs(subset, used)
                    subset.pop()
                    used[i] = False
        used = [False]* len(nums)
        dfs([], used)
        return ret