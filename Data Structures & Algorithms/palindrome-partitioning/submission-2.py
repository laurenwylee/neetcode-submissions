class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        subset = []
        dp = [[None] * len(s) for _ in range(len(s))]
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
            
        def dfs(i, j):
            if j > len(s):
                return
            if dp[i][j - 1] == None:
                dp[i][j - 1] = isPalindrome(s[i:j])
            palindrome = dp[i][j - 1]
            if palindrome:
                subset.append(s[i:j])
                if j == len(s):
                    ret.append(subset.copy())
                dfs(j, j + 1)
                subset.pop()
            dfs(i, j + 1)
        dfs(0, 1)
        return ret
