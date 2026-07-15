class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        for c in t:
            t_dict[c] += 1
        return s_dict == t_dict