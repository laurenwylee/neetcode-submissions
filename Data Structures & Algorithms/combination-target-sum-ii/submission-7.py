class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        subset = []
        def dfs(i, val):
            if i >= len(candidates) and val == target:
                ret.append(subset.copy())
                return 
            if i >= len(candidates) or val > target:
                return
            subset.append(candidates[i])
            dfs(i + 1, val + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, val)
        dfs(0, 0)
        return ret
