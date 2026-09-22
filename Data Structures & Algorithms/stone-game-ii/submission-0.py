class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(alice, i, M):
            if i >= len(piles):
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]
            total = 0
            if alice:
                result = 0
            else:
                result = math.inf
            for X in range(2 * M ):
                if i + X >= len(piles):
                    break
                total += piles[i + X]
                if alice:
                    result = max(result, total + dfs(not alice, i + X + 1, max(M, X + 1)))
                else:
                    result = min(result, dfs(not alice, i + X + 1, max(M, X + 1)))
            dp[(alice, i, M)] = result
            return dp[(alice, i, M)]
        return dfs(True, 0, 1)
