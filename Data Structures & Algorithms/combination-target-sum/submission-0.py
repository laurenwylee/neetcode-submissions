class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(nums, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(len(nums)):
                if target - nums[i] < 0:
                    break
                path.append(nums[i])
                dfs(nums[i:], target - nums[i], path.copy())
                path.pop()

        dfs(nums, target, []) 
        return result