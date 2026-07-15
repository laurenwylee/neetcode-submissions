class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        m = 0
        l = 0
        r = 1
        while r < len(s):
            while s[r] in s[l:r]:
                l+=1
            m = max(m, r-l + 1)
            r+=1
        return m
