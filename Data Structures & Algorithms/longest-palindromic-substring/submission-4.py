class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[None] * len(s) for _ in range(len(s))]
        # abcdedf
        longest = 1
        curr_longest = s[0]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if dp[i][j] != None:
                    continue
                if i == j:
                    dp[i][j] = True
                    continue
                if s[i] == s[j] and (i == j + 1 or dp[j + 1][i - 1] == True):
                    dp[j][i] = True
                    dp[i][j] = True
                    if (i - j) + 1 > longest:
                        longest = (i - j) + 1
                        curr_longest = s[j:i + 1]
                else:
                    dp[j][i] = False
                    dp[i][j] = False
        return curr_longest