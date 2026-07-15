class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        ma = 0
        while r < len(s):
            if s[r] in s[l:r]:
                while s[r] in s[l:r]:
                    l += 1
            else:
                if (r - l) + 1 > ma:
                    ma = (r - l) + 1
            r += 1
        return ma