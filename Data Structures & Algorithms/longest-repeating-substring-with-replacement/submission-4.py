class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        m = 0
        for r in range(len(s)):
            count[s[r]] += 1
            m = max(count[s[r]], m)
            if((r - l + 1) - m > k):
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res