class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(coins, amt):
            if amt == 0:
                return 0
            
            ret = 1e9
            for x in coins:
                if x <= amt:
                    l = amt - x
                    if l not in memo:
                        memo[l] = dfs(coins, l)
                    a = memo[l]
                    ret = min(ret, a + 1)
            return ret

        ret = dfs(coins, amount)
        if ret == 1e9:
            return -1
        return ret
        