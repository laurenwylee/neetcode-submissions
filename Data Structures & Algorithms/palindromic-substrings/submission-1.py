class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            dp[i] = 1 + dp[i-1]
            j = 0
            while j < i:
                if isPalindrome(s[j:i+1]):
                    dp[i] += 1
                j += 1
        return dp[len(s) - 1]