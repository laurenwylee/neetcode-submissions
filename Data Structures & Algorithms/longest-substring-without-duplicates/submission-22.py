class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        substring = defaultdict(int)
        lastSeen = {}
        maximum_length = 0
        while r < len(s):
            if substring[s[r]] < 1:
                substring[s[r]] += 1
                lastSeen[s[r]] = r
            else:
                while l != lastSeen[s[r]] + 1:
                    substring[s[l]] -= 1
                    l += 1
                lastSeen[s[r]] = r
                substring[s[r]] += 1
            r += 1
            maximum_length = max(maximum_length, r - l)
        return maximum_length
            
