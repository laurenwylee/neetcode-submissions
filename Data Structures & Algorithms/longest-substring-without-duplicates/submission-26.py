class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = {}
        longest = 0
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            else:
                longest = max(longest, r - l + 1)
            seen[s[r]] = r
            r += 1
        return longest
            
