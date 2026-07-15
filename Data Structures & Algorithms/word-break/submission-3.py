class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]
            l = 0
            r = 0
            while r < len(s):
                if s[l:r + 1] in wordDict:
                    if dfs(s[r+1:len(s)]):
                        memo[s] = True
                        return True
                r += 1
            memo[s] = False
            return False
        return dfs(s)
