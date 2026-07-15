class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []
        candidates.sort()
        def dfs(i, sum):
            if sum > target:
                return
            if sum == target:
                results.append(subset.copy())
                return
            if i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i + 1, sum + candidates[i])
            subset.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            if i < len(candidates):
                dfs(i, sum)
        dfs(0, 0)
        return results
            

