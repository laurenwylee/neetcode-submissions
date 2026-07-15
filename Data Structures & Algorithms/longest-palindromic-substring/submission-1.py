class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            l = i
            r = i + 1
            re = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(longest):
                        longest = s[l:r+1]
                else:
                    break
                l -= 1
                r += 1
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(longest):
                        longest = s[l:r+1]
                else:
                    break
                l -= 1
                r += 1
        return longest

                
        