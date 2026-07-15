class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count = defaultdict(int)
        ma = 0
        while r < len(s):
            count[s[r]] += 1
            m = [None, 0]
            # get the max freq
            for x in count:
                if count[x] > m[1]:
                    m[0] = x
                    m[1] = count[x]
            while ((r - l) + 1) - m[1] > k:
                count[s[l]] -= 1
                if m[0] == s[l]:
                    for x in count:
                        if count[x] > m[1]:
                            m[0] = x
                            m[1] = count[x]
                l += 1
            ma = max(((r - l) + 1),ma)
            r += 1
        return ma
                    

            
