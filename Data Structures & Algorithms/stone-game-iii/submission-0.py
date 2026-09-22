class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * (len(stoneValue) +  1)
        for i in range(len(stoneValue) - 1, -1, -1):
            total = 0
            best = float('-inf')
            for k in range(0, 3):
                if i + k >= len(stoneValue):
                    break
                total += stoneValue[i + k]
                best = max(best, total - dp[i + k + 1])
            dp[i] = best
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
                
