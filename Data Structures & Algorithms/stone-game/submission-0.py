class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0] * len(piles) for _ in range(len(piles))]
        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] != 0:
                return dp[l][r]
            if (r - l + 1) % 2 == 0:
                isAlice = True
            else:
                isAlice = False
            if isAlice:
                left = piles[l]
                right = piles[r]
            else:
                left = 0
                right = 0
            dp[l][r] = max(left + dfs(l + 1, r), right + dfs(l, r - 1))
            return dp[l][r]

        alice =  dfs(0, len(piles) - 1)
        bob = sum(piles) - alice
        return alice > bob
        
