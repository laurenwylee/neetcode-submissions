class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(j, i):
            while j <= i:
                if s[i] != s[j]:
                    return False
                j += 1
                i -= 1
            return True
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            dp[i] = 1 + dp[i - 1]
            j = i - 1
            while j >= 0:
                if isPalindrome(j, i):
                    dp[i] += 1
                j -= 1
        return dp[len(s) - 1]