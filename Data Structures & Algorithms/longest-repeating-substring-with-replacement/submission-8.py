class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = k - 1
        longest = r - l + 1
        seen = defaultdict(int)
        curr_maximum = 0
        for i in range(k):
            seen[s[i]] += 1
            curr_maximum = max(seen[s[i]], curr_maximum)

        r += 1
        while r < len(s):
            seen[s[r]] += 1
            curr_maximum = max(seen[s[r]], curr_maximum)
            while (r - l + 1) - curr_maximum > k and l < r:
                seen[s[l]] -= 1
                l += 1
                curr_maximum = max(seen[s[l]], curr_maximum)
            longest = max(longest, r - l + 1)
            r += 1

        return longest

