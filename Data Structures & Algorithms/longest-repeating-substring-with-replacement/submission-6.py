class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s):
            return len(s)
        l = 0
        r = 0
        d = {}
        maxChar = 0
        maxSequence = 0
        if s[r] not in d:
            d[s[r]] = 1
        else:
            d[s[r]] += 1
        maxChar = max(maxChar, d[s[r]])
        while r < len(s):
            if k < ((r - l + 1) - maxChar):
                d[s[l]] -= 1
                l += 1
            else:
                maxSequence = max(maxSequence, r - l + 1)
                r+= 1
                if r < len(s):
                    if s[r] not in d:
                        d[s[r]] = 1
                    else:
                        d[s[r]] += 1
                    maxChar = max(maxChar, d[s[r]])
        return maxSequence

            

            
                