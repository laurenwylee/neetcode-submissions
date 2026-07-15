class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []
        curr = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                result.append(curr.copy())
                return
            if i == len(candidates) or curr_sum > target:
                return
            curr.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])
            curr.pop()
            elem = candidates[i]
            j = i + 1
            while j < len(candidates) and candidates[j] == elem:
                j += 1
            dfs(j, curr_sum)
        dfs(0, 0)
        return result