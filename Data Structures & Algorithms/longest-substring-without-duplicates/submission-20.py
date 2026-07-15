class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        seen = {}
        m = 1
        l = 0
        r = l
        # seen[s[l]] = l
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
                seen[s[r]] = r
                r = r + 1
            else:
                seen[s[r]] = r
                m = max((r - l + 1), m)
                r += 1
        return m
             