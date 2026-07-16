class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        subset = []
        dp = [[None] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                dp[i-1][i] = True
            else:
                dp[i-1][i] = False
        n = len(s)
        for length in range(3, n + 1): 
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        ret = []
        subset = []
        def dfs(i, j):
            if i >= n:
                ret.append(subset.copy())
                return
            if j >= n:
                return
            if dp[i][j]:
                subset.append(s[i:j+1])
                dfs(j + 1, j + 1)
                subset.pop()
            dfs(i, j + 1)
        dfs(0, 0)
        return ret

                


            