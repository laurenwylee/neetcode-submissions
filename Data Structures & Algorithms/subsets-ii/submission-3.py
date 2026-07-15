class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        ret = []
        def dfs(i):
            if i >= len(nums):
                ret.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            if i <= len(nums):
                dfs(i)
        dfs(0)
        return ret