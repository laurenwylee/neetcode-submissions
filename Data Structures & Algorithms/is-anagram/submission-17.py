class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for i in t:
            t_dict[i] += 1
        return s_dict == t_dict