class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        d = {}
        l = 0
        d[s[l]] = l
        r = 1
        max_len = 1
        while r < len(s):
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]] + 1
            d[s[r]] = r
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

        

