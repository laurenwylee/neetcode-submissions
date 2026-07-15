class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        d = defaultdict(int)
        for i in s1:
            d[i] += 1
        while r < len(s2):
            de = defaultdict(int)
            for i in s2[l:r+1]:
                de[i] += 1
            if d == de:
                return True
            l += 1
            r += 1
        return False
