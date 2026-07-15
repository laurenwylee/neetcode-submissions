class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = len(t) - 1
        need = defaultdict(int)
        have = defaultdict(int)
        for x in t:
            need[x] += 1
            have[x] = 0
        for x in s[l:r]:
            if x in need:
                have[x] += 1
        mi = len(s)
        ms = ""
        while r < len(s):
            if s[r] in need:
                have[s[r]] += 1
            d = True
            for x in have:
                if have[x] < need[x]:
                    d = False
            if d:
                while ((r - (l+1)) + 1) >= len(t) and ((s[l] not in need )or (have[s[l]] - 1 >= need[s[l]])):
                    if s[l] in need:
                        have[s[l]] -= 1
                    l += 1
                if (r - l) + 1 <= mi:
                    mi = (r - l) + 1
                    ms = s[l:r+1]
            r += 1
        return ms

            