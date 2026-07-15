class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def dfs(subset, used):
            if len(subset) == len(nums):
                results.append(subset.copy())
                return 
            for i in range(len(used)):
                if used[i] == False:
                    used[i] = True
                    subset.append(nums[i])
                    dfs(subset, used)
                    used[i] = False
                    subset.pop()
        dfs([], [False] * len(nums))
        return results