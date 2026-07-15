class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        used = [False] * len(nums)
        def dfs(i):
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            for j in range(len(used)):
                if used[j] == False:
                    curr.append(nums[j])
                    used[j] = True
                    dfs(j)
                    curr.pop()
                    used[j] = False
        dfs(0)
        return result

