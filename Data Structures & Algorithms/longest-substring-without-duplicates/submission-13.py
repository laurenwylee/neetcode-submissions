class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        d = {}
        l = r = 0
        maxlength = 1
        while r < len(s):
            if s[r] in d:
                l = max(d[s[r]] + 1,l)
            d[s[r]] = r
            maxlength = max(r-l+1, maxlength)
            r += 1
        return maxlength
        



        

