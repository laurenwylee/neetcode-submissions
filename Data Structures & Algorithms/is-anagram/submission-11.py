class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = defaultdict(int)
        tmap = defaultdict(int)
        for i in s:
            smap[i] += 1
        for i in t:
            tmap[i] += 1
        return smap == tmap